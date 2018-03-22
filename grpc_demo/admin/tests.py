#-*- coding:utf-8 -*-
from django.test import TestCase
import json

from admin.imp_admin import EventAdmin, PropertyHandler 
from event.models import NewEventParagraph, NewEventTable, Property
# Create your tests here.

ea = EventAdmin()
def test_insert():
    ea.insert_event(json.dumps(event))

def test_update():
    event = {
        'id': 166261, 
        'title': '测试标题烦心',
        'scale': '1001+',
        'begin_time': '2017-12-15 8:00',
        'end_time': '2017-11-17 18:00',
        'city_id': '99',
        'cat_id': '9',
        'tags_id': ['16284', '901'],
        'imgs_id': ['241029', '241027'],

        'venue_title': '测试场馆',
        'venue_address': '测试场馆位置',

        'sponsor_list': [{'id': '30121', 'name': 'update测试主办方000'}, {'name': 'new测试主办方002'}],

        'ticket_list': [
            {
            'id': 69656,
            'price': '23.3333',
            'ticket_name': 'update会务费',
            'begin_time': '2017-12-15 8:00',
            'end_time': '2016-12-17 18:00',
            'description': '不含早餐',
            'min_stock': '2',
            'stock': '880',
            'status': '1',
            },
            {
            'price': '29.3333',
            'ticket_name': 'new会务费2',
            'begin_time': '2016-12-11 8:00',
            'end_time': '2016-12-11 18:00',
            'description': '含早餐',
            'min_stock': '8',
            'stock': '76',
            'status': '0',
            }
        ],


        'price_type': '4', 
        'previous_id': ['166259', '166260'], 


        'from_info_list': [
            {
            'id': 55880,
            'contacts': 'update小时',  
            'telephone': '18234086185',  
            'email': 'updateesd@12.com',  
            'url': 'updatehttps://ww.huo.com',  
            'type_id': '2',  
            'source': '5',  # 来源
            },
            {
            'contacts': 'new小时002',  
            'telephone': '2823486185',  
            'email': 'qqesd@12.com',  
            'url': 'https://qww.huo.com',  
            'type_id': '3',  
            },
        ],


        'review_list':[
                {
                    'id': 33231,
                    'url': 'http://docpath',
                    'description': 'update领导们',
                },
                {
                    'url': 'http://docpath',
                    'description': 'new同学们',
                },
        ]
    }
    ea.insert_event(json.dumps(event))


a_tree = [
    {
    'name': '会议日程',
    'leaf': False,
    'children': [
        {
        'name': '第一天',
        'leaf': False,
        'children': [
            {
            'leaf': True,
            'name': '',
            'type': 'text',
            'value': '大会的第一天将在美丽的迎西校区举行',
            }
            ]
        },

        {
        'name': '第二天',
        'leaf': False,
        'children': [
            {
            'leaf': True,
            'name': '',
            'type': 'text',
            'value': '大会的第二天将在美丽的迎西校区举行',
            }
            ]
        },
    ]
    },
    
    {
        'name': '会议嘉宾',
        'leaf': False,
        'children':[
            {'leaf': True, 'type': 'text', 'value': '嘉宾文本'}, 
            {'leaf': True, 'type': 'guest', 'value': {'name': '小史', 'company': '豆瓣'}}, 
        ]
    }
]


json_list = []
def pre_order(tree):
    node_list = []

    for node in tree:
        if node.get('leaf') is False:
            node_list.append(pre_order(node.get('children')))
        else:
            type_dict = {
                'text': 0, 
                'guest': 1, 
                'int': 2, 
            }
            node_list.append({'type': type_dict[node.get('type')]})

    return node_list


def convert_flat(tree, father_name='#', stack=[]):
    for node in tree:
        stack.append({'father_name': father_name, 'name': node.get('name')})
        if node.get('leaf') is False:
            convert_flat(node.get('children'), node.get('name'), stack)
    return stack



def great_gaint():
    data = [
        {
            'name': 'root',  
            'left': 1,  
            'right': 10,  
            'level': 0,
        },
        {
            'name': '会议日程',  
            'left': 4,  
            'right': 9,  
            'level': 1,
        },
        {
            'name': '会议介绍',  
            'left': 2,  
            'right': 3,  
            'level': 1,
            'value': '会议介绍',
        },
        {
            'name': '第一天',  
            'left': 5,  
            'right': 6,  
            'level': 2,
            'value': '第一天日程是'
        },
        {
            'name': '第二天',  
            'left': 7,  
            'right': 8,  
            'level': 2,
            'value': '第二天日程是'
        },
    ]


def get_nest_list(node):   
    '''
    recursive find children, construct a nest list.
    '''
    if node.is_leaf_node():
        return {'name': node.name, 'leaf': True}
    else:
        child_list = []
        for _node in node.get_children():
            child_list.append(get_nest_list(_node))
        return {'name': node.name, 'leaf': False, 'children': child_list}

def get_nest_list_v2(node):   
    '''
    recursive find children, construct a nest list.
    '''
    children_list = []
    for _node in node.get_children():
        import ipdb
        ipdb.set_trace()
        if _node.is_leaf_node():
            children_list.append({
                'name': _node.name,
                'leaf': True,
                'value': _node.paragraph.txt,
            })
        else:
            children_list.append({
                'name': _node.name,
                'leaf': False,
                'children': get_nest_list_v2(_node)
            })
    return children_list

def get_nest_list_test():
    root = Property.objects.filter(lft=1).last()
    return get_nest_list_v2(root)


def total_test():
    event_id = 25
    ph = PropertyHandler(event_id)
    data = [
        {
            'name': 'root',  
            'left': 1,  
            'right': 10,  
            'level': 0,
        },
        {
            'name': '会议日程',  
            'left': 4,  
            'right': 9,  
            'level': 1,
        },
        {
            'name': '会议介绍',  
            'left': 2,  
            'right': 3,  
            'level': 1,
            'value': '会议介绍',
        },
        {
            'name': '第一天',  
            'left': 5,  
            'right': 6,  
            'level': 2,
            'value': '第一天日程是'
        },
        {
            'name': '第二天',  
            'left': 7,  
            'right': 8,  
            'level': 2,
            'value': '第二天日程是'
        },
    ]
    ph.insert_properties(data)
    x = ph.get_nest_properties()
    y = ph.get_flat_properties()
    from pprint import pprint
    pprint(x)
    pprint(y)
