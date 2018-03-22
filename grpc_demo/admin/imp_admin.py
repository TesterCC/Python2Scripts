#-*- coding:utf-8 -*-
import time
import simplejson as json 
import random
import copy
from decimal import Decimal
import traceback
import logging
import datetime

import admin_pb2

from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, CHANGE


from tag.models import NewEventTag
from cat.models import NewEventCat
from city.models import NewDistrict
from guest.models import GuestCompany, GuestJob, Guest
from event.models import NewEventFrom, NewEventPriceUnit, NewEventPrice,\
        NewEventParagraph, NewEventTable, Property, Statistic, XEvent
from news_link.models import NewsLink
from sponsor.models import NewSponsor
from venue.models import NewVenue
from eventreview.models import EventReview
from utils.text_ctrl import text_ctrl
from utils.distributed_lock import dlm

log = logging.getLogger('website.debug')


class LockAcquireFailedException(Exception):
    # can't acquire redis lock.
    pass

class PropertyHandler:
    def __init__(self, event_id, event):
        '''
        @param event type: NewEventTable
        '''
        self.event_id = event_id
        self.event = event

    def keep_old_structure(self):
        '''
        insert into guests and paragraph relation to event.
        '''
        pass

    def get_nest_properties(self):
        root = Property.objects.filter(event_id=self.event_id, lft=1).order_by('-tree_id').first()
        return self._get_nest_list_v2(root)


    def get_flat_properties(self):
        root = Property.objects.filter(event_id=self.event_id, lft=1).order_by('-tree_id').first()
        if not root:
            return []
        properties = root.get_descendants()

        # 此id供前端使用
        id_count = 1
        properties_list = [
            {
                'name':  root.name,
                'en_name': root.en_name,
                'left': root.lft,
                'right': root.rght,
                'level': root.level,
                'type': root.leaf_type,
                'id': id_count,
            }
        ]
        for p in properties:
            _property = {}
            id_count += 1
            _property['name'] = p.name
            _property['en_name'] = p.en_name
            _property['left'] = p.lft
            _property['right'] = p.rght
            _property['level'] = p.level
            _property['type'] = p.leaf_type
            _property['id'] = id_count
            _property['children'] = []
            _property['value'] = ''
            if p.is_leaf_node():
                _property['value'] = p.paragraph.txt
                # 是嘉宾
                if p.leaf_type == 2:
                    children = list(p.guest.values('id', 'name', 'img__urls', 'company__name', 'job__name', 'img_id', 'img__server__name'))
                    for child in children:
                        child['company'] = child['company__name']
                        child['job'] = child['job__name']
                        if child['img_id']:
                            child['url'] = child['img__server__name'] + child['img__urls']
                        else:
                            child['url'] = None
                    _property['children'] = children


                # 是图表数据
                elif p.leaf_type == 1:
                    _property['children'] = json.loads(p.statistic.json_field)
            properties_list.append(_property)
        return properties_list


    def insert_properties(self, data):
        if data == []: 
            return None

        # left从小到大排列, 即为深度优先搜索时的顺序
        data = sorted(data, key=lambda x: x.get('left'))
        # stack 用于存储包含子节点的节点
        stack = []
        root = data.pop(0)
        p_root = Property.objects.create(event_id=self.event_id, name='root')
        root['model'] = p_root
        stack.append(root)
        paragraph_id_list = []
        while data:
            node = data.pop(0)
            p = Property.objects.create(parent=stack[-1].get('model'), 
                        event_id=self.event_id,
                         name=node.get('name'))

            left = node.get('left')
            right = node.get('right')

            # 存在子节点, 则入栈
            if left + 1 != right:
                node['model'] = p
                stack.append(node)
            # 保存叶子节点的文本
            else:
                # 保存站外图片， 修改img src 为活动家本站图片
                txt = node.get('value')
                text = NewEventParagraph.objects.create(txt=text_ctrl.replace_text_image(txt), name=node.get('name'))
                p.paragraph = text 

                # 为了兼容, 以后删去
                paragraph_id_list.append(text.id)
                # end 为了兼容, 以后删去
                if node.get('type') == 2:
                    #是嘉宾
                    self.save_guest(p, node.get('children'))
                    p.leaf_type = 2
                else:
                    # 叶子节点有children且type不为2，则是有饼状图数据。
                    children = node.get('children', None)
                    if children:
                        s = Statistic.objects.create(json_field=json.dumps(children))
                        p.statistic = s
                        p.leaf_type = 1
                p.save()
            # end of 保存叶子节点的文本


            # 此节点的所有子节点均已访问过, 从栈中弹出此节点。
            if right + 1 == stack[-1].get('right'):
                stack.pop()

        # 为了兼容, 以后删去
        self.event.paragraph.clear()
        self.event.paragraph.add(*paragraph_id_list)
        # end 为了兼容, 以后删去

    def _get_nest_list_v2(self, node):
        '''
        recursive find children, construct a nest list.
        '''
        children_list = []
        for _node in node.get_children():
            if _node.is_leaf_node():
                # TODO check leaf node type, get guest and statistics info.
                children_list.append({
                    'name': _node.name,
                    'en_name': _node.en_name,
                    'leaf': True,
                    'value': _node.paragraph.txt,
                })
            else:
                children_list.append({
                    'name': _node.name,
                    'en_name': _node.en_name,
                    'leaf': False,
                    'children': self._get_nest_list_v2(_node)
                })
        return children_list


    def save_guest(self, node, guests):
        '''
        修改嘉宾信息，并保存 节点<->嘉宾 的对应关系
        @param node type:  event.models Property.
        '''
        guests_id_list = []
        for _guest in guests:
            _id = _guest.get('id', 0)
            _img_id = None if not _guest.get('img_id', None) else _guest.get('img_id')
            _name = _guest.get('name', '')
            _job = _guest.get('job', '')
            _company = _guest.get('company', '')
            # model 定义时，限制了此不能为NULL。
            if _job is None:
                _job = ''
            #不知道为啥,get_or_create经常会创建两个.所以还是用filter.first
            #company, _ = GuestCompany.objects.get_or_create(name=_company)
            company = GuestCompany.objects.filter(name=_company).first()
            if not company:
                company = GuestCompany.objects.create(name=_company)
                company.save()
            job = GuestJob.objects.filter(name=_job).first()
            if not job:
                job = GuestJob.objects.create(name=_job)
                job.save()
            #job, _ = GuestJob.objects.get_or_create(name=_job)
            # 若id已存在，则修改数据。不存在，则新增
            log.debug((11111,_id,333333))
            if _id == 0:

                log.debug(u'guest name is {}'.format(_name))
                guest, _ = Guest.objects.get_or_create(name=_name, job=job, company=company, img_id=_img_id)
                guests_id_list.append(guest.id)
            else:
                log.debug((1111111111111111111,_id))
                log.debug((_name,job,company,_img_id))
                #Guest.objects.filter(id=_id).update(name=_name, job=job, company=company, img_id=_img_id)
                guestquery = Guest.objects.filter(id=_id)
                guestquery.update(name=_name, job_id=job.id, company_id=company.id, img_id=_img_id)
                guests_id_list.append(_id)
        node.guest.add(*guests_id_list)
        # 兼容老版，嘉宾页未做更新则不修改。
        self.event.guest.clear()
        self.event.guest.add(*guests_id_list)


class EventAdmin:
    def generate_old_event_id(self, id_):
        '''
        根据sys_new_event_info 的id 生成 old_event_id。
        old_event_id: 生成活动链接时使用

        @type id_: int
        @rtype: int
        '''
        if id_:
            try:
                NewEventTable.objects.get(old_event_id=id_)
                return self.generate_old_event_id(random.randint(1,2000000000))
            except:
                return id_


    def _insert(self, json_request, user_id):
        #TODO 最后编辑人   日志记录
        # rel time , edit, last_edit,  update_time
        #TODO raise 不同的Error, 并猜测不同的理由返回。

        #TODO 城市拼音能够选出城市    
        event_json = json.loads(json_request)

        # 基础数据，插入到主表
        id_ = event_json.get('id', 0)
        isshow_id = event_json.get('isshow_id', 5) # 0
        name = event_json.get('name', '')
        scale = event_json.get('scale', '1000') # 规模
        introduction = event_json.get('introduction', '') # 规模

        begin_time = event_json.get('begin_time', '')
        end_time = event_json.get('end_time', '')
        # charge = event_json.get('charge', '0') # 是否付费推广 为什么这里会对接point字段???
        # if not charge.isdigit():
            # charge = '0'

        if id_:
            NewEventTable.objects.filter(id=id_).update(
                name=name,
                search=name,
                begin_time=datetime.datetime.strptime(begin_time, '%Y-%m-%d %H:%M'),
                end_time=datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M'),
                scale=scale,
                isshow_id=isshow_id,
                last_edit_id=user_id,
                content=introduction,
                #point=charge,
            )
            event = NewEventTable.objects.get(id=id_)
        else:
            event = NewEventTable.objects.create(
                name=name,
                search=name,
                begin_time=datetime.datetime.strptime(begin_time, '%Y-%m-%d %H:%M'),
                end_time=datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M'),
                scale=scale,
                isshow_id=isshow_id,
                edit_id=user_id,
                last_edit_id=user_id,
                content=introduction,
                #point=charge,
            )

        # 写入操作日志
        event_replica = copy.deepcopy(event_json)
        event_replica.pop('event_content')
        LogEntry.objects.log_action(
            user_id=user_id,
            content_type_id = ContentType.objects.get_for_model(event).pk,
            object_id = event.pk,
            object_repr = u'修改活动',
            action_flag = CHANGE,
            #change_message = u'', 
            change_message = json.dumps(event_replica), 
        )
        # end 写入操作日志

        # end 基础数据，插入到主表
        
        # city, cat, tags, imgs
        city_id = event_json.get('city_id', 101) # 城市主键 id 
        cat_id = event_json.get('cat_id', 2)
        tags = event_json.get('tags', [])
        imgs = event_json.get('imgs', [])# 这里改成了多加一个url参数的字典列表
        previous_id = event_json.get('previous_id', [])
        news_id = event_json.get('news_id', [])

        # 需要type check 的是 需要保存成int的或者需要查询int的数据
        if not isinstance(city_id, (int, str, unicode)):
            city_id = '101'
        if not isinstance(cat_id, (int, str, unicode)):
            cat_id = '2'
        if not isinstance(tags, list):
            tags = []
        if not isinstance(imgs, list):
            imgs = []

        log.debug(previous_id)
        if not isinstance(previous_id, list):
            previous_id = []

        # 确保list内是id.
        for _index, _previous in enumerate(previous_id):
            if isinstance(_previous, (str, unicode)):
                if not _previous.isdigit():
                    previous_id.pop(_index)
            elif not isinstance(_previous, int):
                # 既不是int，也不是str
                previous_id.pop(_index)

        log.debug(previous_id)
        log.debug(news_id)
        if not isinstance(news_id, list):
            news_id = []
        for _index, _news_id in enumerate(news_id):
            if isinstance(_news_id, (str, unicode)):
                if not _news_id.isdigit():
                    news_id.pop(_index)
            elif not isinstance(_news_id, int):
                # 既不是int，也不是str
                    news_id.pop(_index)
        log.debug(news_id)
        # end type check

        event.city.clear()
        event.city.add(city_id)
        event.cat.clear()
        event.cat.add(cat_id)

        event.tag.clear()
        tags_id = []
        for _tag in tags:
            tag, _ = NewEventTag.objects.get_or_create(name=_tag['name'])
            tags_id.append(tag.id)

        event.tag.add(*tags_id)

        event.img.clear()
        event.img.add(*[_img.get('id') for _img in imgs])
        event.previous.clear() # 往届会议
        event.previous.add(*previous_id)

        NewsLink.objects.filter(event_id=event.id).delete()
        NewsLink.objects.bulk_create([NewsLink(event_id=event.id, wp_post_id=_id) for _id in news_id])

        # venue
        venue_title = event_json.get('venue_title', '')
        venue_address = event_json.get('venue_address', '')
        # venue, _ = NewVenue.objects.get_or_create(city_id=city_id, title=venue_title,
        #         address=venue_address)  
        venue = NewVenue.objects.filter(city_id=city_id, title=venue_title,
                 address=venue_address).first()  
        if not venue:
            venue = NewVenue.objects.create(city_id=city_id, title=venue_title,
                 address=venue_address)
        event.addr.clear()
        event.addr.add(venue)

        event.save()

        # --- 开始了比较复杂的逻辑 God Bless!
        # 主办方
        self.save_sponsor(event.id, event_json.get('sponsor_list', []))

        # 票价
        self.save_ticket(event.id, event_json.get('ticket_list', []))

        # 活动类型 
        event.Price = NewEventPrice.objects.create(
                Type_id=event_json.get('price_type', 4), Currency_id=1)

        # 来源信息
        self.save_from_info(event, event_json.get('from_info_list', []))

        #TODO 生成 old_event_id
        if not event.old_event_id:
            event.old_event_id = self.generate_old_event_id(random.randint(1, 2000000000))
        event.save()

        # 此会议的精彩回顾
        self.save_review(event, event_json.get('review_list', []))

        
        event.save()

        prop_handler = PropertyHandler(event.id, event)
        prop_handler.insert_properties(event_json.get('event_content', []))

        # insert to sys_x_event, sys_x_event is for list page. e.g. /beijing/it/03/
        if isshow_id == 1:
            if XEvent.objects.filter(old_event_id=event.old_event_id).exists():
                XEvent.objects.filter(old_event_id=event.old_event_id).update(
                    cat_id=cat_id,
                    city_id=city_id,
                    begin_time=datetime.datetime.strptime(begin_time, '%Y-%m-%d %H:%M')
                )
            else:
                pv = event.visit or 0
                XEvent.objects.create(old_event_id=event.old_event_id, cat_id=cat_id, city_id=city_id, begin_time=datetime.datetime.strptime(begin_time, '%Y-%m-%d %H:%M'), pv=pv)
        else:
            XEvent.objects.filter(old_event_id=event.old_event_id).delete() 
        # end insert
        return event.id

    def save_sponsor(self, event_id, sponsors):
        '''
        实际上没有使用 id 了  2017-02-12
        '''
        old_sponsors_id = NewSponsor.objects.filter(events__id=event_id).values_list('id', flat=True)
        old_sponsors_str_id = [str(_id) for _id in old_sponsors_id]

        new_sponsors_str_id = []
        for _sponsor in sponsors:
            _id = _sponsor.get('id', 0)
            _name = _sponsor.get('name', '')
            # 若id已存在，则修改数据。不存在，则新增
            if _id == 0:
                sponsor = NewSponsor.objects.filter(name=_name).first()
                if sponsor is None:
                    sponsor = NewSponsor.objects.create(name=_name)
                #sponsor, _ = NewSponsor.objects.get_or_create(name=_name)
                sponsor.events.add(event_id)
            else:
                NewSponsor.objects.filter(id=_id).update(name=_name)
                # 新增此关联
                new_sponsors_str_id.append(str(_id))

        # 删除此次提交未提到的主办方与活动的关联
        delete_sponsor_id = set(old_sponsors_str_id) - set(new_sponsors_str_id) 
        for _sponsor in NewSponsor.objects.filter(id__in=delete_sponsor_id):
            _sponsor.events.remove(event_id)


    def save_review(self, event, review):
        old_reviews_id = event.eventreview.values_list('id', flat=True)
        old_reviews_str_id = [str(_id) for _id in old_reviews_id]

        new_reviews_str_id = []
        for _review in review:
            _id = _review.get('id', 0)
            url = _review.get('url', '')
            description = _review.get('description', '')
            if _id == 0:
                review = EventReview.objects.create(doc_path=url, doc_desc=description)
                #FIXME 这里保存可能不生效, 带测试
                event.eventreview.add(review)
            else:
                EventReview.objects.filter(id=_id).update(doc_path=url, doc_desc=description)
                new_reviews_str_id.append(str(_id))

        # 删除此次提交未提到的精彩回顾
        delete_reviews_id = set(old_reviews_str_id) - set(new_reviews_str_id) 
        #FIXME 这里保存可能不生效, 带测试
        event.eventreview.remove(*delete_reviews_id)
        


    def save_from_info(self, event, from_info_list):
        '''
        保存来源信息
        实际上是活动和它是一对多的关系，因此取出修改而不是强行创建
        '''
        old_from_info_id = event.from_info.values_list('id', flat=True)
        old_from_info_str_id = [str(_id) for _id in old_from_info_id]

        new_from_info_id = []
        for _from_info in from_info_list:
            _id = _from_info.get('id', 0)
            contacts = _from_info.get('contacts', '')
            telephone = _from_info.get('telephone', '')
            email = _from_info.get('email', '')
            url = _from_info.get('url', '')
            type_id = 1 # 是否联系   这个功能现在已经不使用了
            content = _from_info.get('content', '')
            source = _from_info.get('source', '1')
            if _id == 0:
                new_event_from = NewEventFrom.objects.create(Website=url, contacts=contacts, tel=telephone, content=content, email=email, f_Class_id=source, type_id=type_id)
                event.from_info.add(new_event_from)
            else:
                new_event_from = NewEventFrom.objects.filter(id=_id).update(Website=url, contacts=contacts, tel=telephone, content=content, email=email, f_Class_id=source, type_id=1)
                new_from_info_id.append(str(_id))

        # 删除此次提交未提到的来源信息
        delete_info_id = set(old_from_info_str_id) - set(new_from_info_id) 
        # FIXME 这里保存可能不生效, 带测试
        event.from_info.remove(*delete_info_id)

          
    def save_ticket(self, event_id, tickets_list):
        '''
        保存票价 
        懒得管啦，直接置空已有票价的关联，update和insert都视为insert。2333333
        '''
        log.debug(tickets_list)
        with transaction.atomic():
            NewEventPriceUnit.objects.filter(event_id=event_id).update(event_id=None)

            NewEventPriceUnit.objects.bulk_create([
                NewEventPriceUnit(
                    price=Decimal(_ticket.get('price', 0)), # 费用单价
                    property=_ticket.get('property', ''), # 费用名称
                    begin_time=datetime.datetime.strptime(_ticket.get('begin_time'), '%Y-%m-%d %H:%M'),
                    end_time=datetime.datetime.strptime(_ticket.get('end_time'), '%Y-%m-%d %H:%M'),
                    content=_ticket.get('content', ''), # 费用提供的服务
                    limit_people=_ticket.get('limit_people', 1), # 最小购买量
                    stock=_ticket.get('stock', 999), # 库存
                    status=_ticket.get('status', 1), # 是否有效
                    event_id=event_id,
                    original_price=None if not _ticket.get('original_price', 0) else Decimal(_ticket.get('original_price')),
                )
                for _ticket in tickets_list
                ])

    def insert_event(self, json_request, user_id):
        self.event_response = admin_pb2.EventResponse()

        my_lock = dlm.lock("admin:save:event:mptt", 4000)


        if my_lock is False:
            raise LockAcquireFailedException('can not acquire redis lock, try again')

        try:
            with transaction.atomic():
                self.event_response.event_id = self._insert(json_request, user_id)
                self.event_response.code = 1
                self.event_response.msg = ''
        except Exception as e:
            print(traceback.format_exc())
            print('insert event faield !!!!!!!!!!!!!!!!')
            log.debug('insert event faield !!!!!!!!!!!!!!!!')
            log.debug(traceback.format_exc())
            self.event_response.code = 0
            self.event_response.msg = str(e)


        log.debug('insert success !!!!!!!!!!')
        dlm.unlock(my_lock)

        return self.event_response


    def display_event(self, event_id):
        '''
        渲染数据供前台使用
        '''
        event_data = admin_pb2.EventData()
        event = NewEventTable.objects.get(pk=event_id)

        ret = {}
        ret['id'] = event.id
        ret['old_event_id'] = event.old_event_id
        ret['isshow_id'] = event.isshow_id
        ret['name'] = event.name
        ret['scale'] = event.scale
        ret['introduction'] = event.content
        if event.begin_time:
            ret['begin_time'] = event.begin_time.strftime('%Y-%m-%d %H:%M')
        else:
            ret['begin_time'] = ''
        if event.end_time:
            ret['end_time'] = event.end_time.strftime('%Y-%m-%d %H:%M')
        else:
            ret['end_time'] = ''


        ret['city_id'] = event.city.first().id if event.city.exists() else 101
        ret['city_name'] = event.city.first().district_name if event.city.exists() else u'北京' 
        ret['province_id'] = event.city.first().parent_id if event.city.exists() else 600
        ret['cat_id'] = event.cat.first().id if event.city.exists() else 2
        ret['tags'] = list(event.tag.values('id', 'name'))
        imgs = event.img.values('id', 'urls', 'server__name')
        ret['imgs'] = [{'id': _img['id'], 'url': _img['server__name'] + _img['urls']} for _img in imgs ]
        ret['previous_id'] = list(event.previous.values_list('id', flat=True))
        ret['news_id'] = list(NewsLink.objects.filter(event_id=event.id).values_list('wp_post_id', flat=True))

        venue = event.addr.first()
        if venue:
            ret['venue_title'] = venue.title
            ret['venue_address'] = venue.address

        ret['sponsor_list'] = list(NewSponsor.objects.filter(events=event).values('id', 'name'))

        ret['ticket_list'] = list(NewEventPriceUnit.objects.filter(event=event).values('id', 'price', 'property', 'begin_time', 'end_time', 'content', 'limit_people', 'stock', 'status', 'original_price'))
        for ticket in ret['ticket_list']:
            ticket['begin_time'] = datetime.datetime.strftime(ticket['begin_time'], '%Y-%m-%d %H:%M')
            ticket['end_time'] = datetime.datetime.strftime(ticket['end_time'], '%Y-%m-%d %H:%M')

        try:
            ret['price_type'] = event.Price.Type.id
        except AttributeError:
            ret['price_type'] = 4

        ret['from_info_list'] = list(event.from_info.values('id', 'contacts', 'tel', 'email', 'Website', 'content'))
        for _ret in ret['from_info_list']:
            _ret['telephone'] = _ret['tel']
            _ret['url'] = _ret['Website']
            _ret['content'] = _ret['content']

        ret['review_list'] = list(event.eventreview.values('id', 'doc_path', 'doc_desc'))
        for _ret in ret['review_list']:
            _ret['url'] = _ret['doc_path']
            _ret['description'] = _ret['doc_desc']


        prop_handler = PropertyHandler(event.id, event)
        event_data.json_response = json.dumps({'event': ret,
                     'event_content': prop_handler.get_flat_properties()})
        return event_data


    def get_all_province(self):
        city_json = admin_pb2.CityJSON()

        province = NewDistrict.objects.filter(parent_id=0).order_by('id')
        ret = []
        for _province in province:
            province = {}
            province['id'] = _province.id 
            province['name'] = _province.district_name
            province['child'] = list(_province.children.all().values_list('id', 'district_name'))
            ret.append(province)

        city_json.city = json.dumps(ret)
        return city_json


    def get_all_tag(self):
        tag_json = admin_pb2.TagJSON()
        ret = {}
        for cat in NewEventCat.objects.filter(id__in=[2, 4, 3, 6, 9,118,120,122,124,126,128,96]):
            ret[cat.id] = list(cat.tag.values('id', 'name'))

        tag_json.tag = json.dumps(ret)
        return tag_json


