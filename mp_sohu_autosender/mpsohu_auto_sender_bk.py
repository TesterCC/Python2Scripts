#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/12 17:21'

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

from time import sleep
import json
import re

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

"""
需求：
1.每个账号每天发5篇，无需换IP发布，但需清除cookie，发布间隔3分钟。（不按此规则容易被屏蔽）
2.发帖内容按规定格式提交
18683715921 不可用   IT类别
"""


class AutoSender(object):
    """
    for auto send article
    """

    def __init__(self, username="15281005385", password=""):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            # 'Host': 'www.huodongjia.com',
            'Accept-Encoding': 'gzip',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
        }

        # parser_json_url = "https://www.huodongjia.com/event-1322992792.html?json=1"
        domain_url = "https://www.huodongjia.com/"

        username_related = {
            '18702895635': 'business',  # 全部
            '15281005385': 'medical',  # 医疗医学
            # '18683715921': 'it',  # IT互联网
            '18782291154': 'energy',  # 能源化工
            '18108061758': 'finance',  # 金融财经
        }

        channel_id_related = {
            '18702895635': '34',  # 其他
            '15281005385': '24',  # 医疗医学  健康
            # '18683715921': '30',  # IT互联网  科技
            '18782291154': '34',  # 其他 能源化工
            '18108061758': '15',  # 金融财经
        }

        category_id_related = {
            '18702895635': '901',  # 综合
            '15281005385': '23',  # 医疗医学
            # '18683715921': '911',  # IT互联网
            '18782291154': '901',  # 综合
            '18108061758': '996',  # 金融财经
        }

        # 分类
        usercolumn_id_related = {
            '18702895635': '119133',  # 综合
            '15281005385': '183567',  # 医疗医学  健康产业
            # '18683715921': '119129',  # IT互联网    # cannot use
            '18782291154': '106968',  # 能源行业
            '18108061758': '183584',  # 金融财经  互联网金融
        }

        cat = username_related.get(username, '')
        channel_id = channel_id_related.get(username, '34')
        category_id = category_id_related.get(username, '901')
        usercolumn_id = usercolumn_id_related.get(username, '-1')  # -1 未分类

        # 要考虑翻页
        cat_url = "https://www.huodongjia.com/{0}".format(cat)

        self.headers = headers
        self.username = username
        self.password = password
        self.article_title = u''
        self.content_message = u''
        self.cat_url = cat_url
        self.cat = cat
        self.session = requests.session()
        self.domain_url = domain_url
        # self.retry_num = 5
        # self.i = 1  # it/page flag
        self.send_times = 3  # 设置每个账号的发帖数
        self.interval_time = 60   # 单账户发帖间隔时间，单位秒

        self.channel_id = channel_id
        self.category_id = category_id
        self.usercolumn_id = usercolumn_id

        self.driver = webdriver.PhantomJS()
        self.login_url = "https://mp.sohu.com/mpfe/v3/login"
        self.after_login_url = "https://mp.sohu.com/mpfe/v3/main/first/page"
        self.edit_article_url = "http://mp.sohu.com/v2/main/news/add.action"
        # self.publish_direct_url = "https://mp.sohu.com/v3/news/publish"   # publish
        # self.post_draft_url = "https://mp.sohu.com/v3/news/draft"  # draft
        self.publish_direct_url = "https://mp.sohu.com/v3/news/draft"  # for debug, change publish url to draft url

    def login_platform(self):
        """
        Start to Login and get sohu cookies, will load cookies by requests session directly
        """
        print(">>>" * 10 + "Start to run, initial driver..." + ">>>" * 10)

        self.driver.get(self.login_url)

        login_nav = self.driver.find_element_by_xpath(
            '//*[@id="mpfe"]/div[3]/div/article/div[1]/div[2]/div/div[1]/span[1]')

        login_nav.click()

        input_username = self.driver.find_element_by_xpath(
            "//*[@id='mpfe']/div[3]/div/article/div[1]/div[2]/div/div[3]/div[1]/input")

        input_username.click()

        input_username.send_keys(self.username)

        input_password = self.driver.find_element_by_xpath(
            "//*[@id='mpfe']/div[3]/div/article/div[1]/div[2]/div/div[3]/div[2]/input")

        input_password.click()

        input_password.send_keys(self.password)

        submit = self.driver.find_element_by_xpath('//*[@id="mpfe"]/div[3]/div/article/div[1]/div[2]/div/button')

        submit.click()

        print("Login ... Please wait...")

        sleep(5)

        if self.driver.current_url == self.after_login_url:
            print("Login Success!")
            return True
        else:
            print("Login Failed! Please check it.")
            self.driver.quit()
            return False

    def clear_account_cache(self):
        """
        When end this account task, clear session and cookies
        """
        if self.session:
            self.session.close()
        if self.driver:
            self.driver.delete_all_cookies()
            self.driver.quit()
        sleep(1)
        print(">>>" * 10 + "Finish account cache clear..." + ">>>" * 10)

    def send_article(self):
        # get valid_url_list, 然后循环发贴
        link_list = self.get_event_url_from_cat_url()  # return a url list with 5 url

        valid_link_list = self.check_valid_url(link_list)  # 进入逻辑取检查，返回一个不重复的link_list

        # i = 0  # 单账号发贴初始值
        # for valid_url in valid_link_list:
        #     while i < self.send_times:
        #         valid_json_url = valid_url + "?json=1"
        #         self.publish_article(valid_json_url)
        #         i += 1
        #         print("Finish {0} article send".format(i))
        #         sleep(10)
        #     print(">>>>>>>>>>>>>>>已达发帖限制数{}".format(self.send_times))
        #     break
        for i in range(len(valid_link_list) - 1):
            while i < self.send_times:
                valid_json_url = valid_link_list[i] + "?json=1"
                self.publish_article(valid_json_url)
                i += 1
                print("Finish {0} article send".format(i))
                sleep(self.interval_time)    # 初始化中可设置
            print(">>>>>>>>>>>>>>>已达发帖限制数{}".format(self.send_times))
            break

    def publish_article(self, valid_url):
        print("---" * 10 + "发表文章" + "---" * 10)

        data = self.get_json_event_info(valid_url)  # get data from website directly

        # Get and Save cookie
        Cookies = self.driver.get_cookies()

        for cookie in Cookies:
            self.session.cookies.set(cookie['name'], cookie['value'])  # cookie持久化

        header = self.session.headers.update(self.headers)

        # print("---------开始正式发表文章----------")

        post_data = {
            'title': data.get('article_title'),
            'brief': '',
            'content': data.get('article_content'),
            'channelId': int(data.get('article_channel_id')),
            'categoryId': int(data.get('article_category_id')),
            # 'id': 227155152,
            'userColumnId': int(data.get('article_usercolumn_id')),  # required
            'isOriginal': 0,
        }

        # print(post_data)

        # Publish article directly
        print("Start send article directly...")
        req = self.session.post(self.publish_direct_url, data=post_data, headers=header)
        if req.status_code == 200:
            print("Published article id is {0}, request status code is {1}".format(req.text, req.status_code))
            print('Publish article success, write into log.')

            log_name = self.create_log()

            with open(log_name, 'at') as log:
                log.write('{}'.format("event-" + str(data.get('event_id')) + ".html") + '\n')
            log.close()
            print('{} has written in {}'.format(data.get('event_id'), log_name))
            return True
        else:
            print("Published article report error: {0}. Request status code is {1}".format(req.text, req.status_code))
            return False

    def get_json_event_info(self, valid_url):
        """
        接收一个url并返回数据
        :param target_url:
        :return: data
        """

        req = requests.get(valid_url, headers=self.headers, timeout=10).content  # python2 str, python3 bytes

        # the JSON object must be str, not 'bytes'
        req = req.decode("utf-8")  # str

        # 将已编码的json字符串解码为Python对象
        req_dict = json.loads(req)

        event_url = self.domain_url + req_dict['event']['event_url'].replace("/", "")  # 不然会有bug

        event_title = req_dict['event']['event_name']

        article_title = u"{0}【活动家】".format(event_title)

        event_id = req_dict['event']['event_id']

        # id = str(req_dict['event']['id'])   ＃ no use
        # event_status = req_dict['event']['event_status'] ＃ no use

        event_begin_time = req_dict['event']['event_begin_time']

        event_end_time = req_dict['event']['event_end_time']

        def get_event_img_v2():
            d_event = req_dict.get('event')
            for item in d_event.get('event_img'):
                return item['server__name'] + item['urls']

        event_img_url = get_event_img_v2()

        def get_event_content():
            """
            获取会议内容html important
            :return:
            """
            d_event = req_dict.get('event')

            for items in d_event.get('properties'):
                for k, v in items.items():
                    if k == 'children':
                        for i in v:
                            return i.get('value')

        event_content = get_event_content()

        event_suffix_pic = "http://5b0988e595225.cdn.sohucs.com/images/20180326/4ad8e52fab2e4552bb107d5bdb7bf1c9.jpeg"

        def get_event_tag_info():
            """
            :return: a tag list with whitespace
            """
            event_tag_list = req_dict['event']['event_tag_info']
            return " ".join(items['name'] for items in event_tag_list)

        event_tag_list = get_event_tag_info()

        article_prefix = u'会议即将召开，<strong>{0}</strong> 详情请上活动家官网查看。 <p>会议网址：</p> {1}  <p> <strong>(请将网址复制到浏览器中打开) </strong> </p> '.format(
            event_title, event_url)

        article_event_content = u'<p style="text-align: center;"><img src="{0}" > </p> <p> {1} </p>'.format(
            event_img_url, event_content)  # content include img

        # article_event_schedule = u'<p>{0}</p>'.format(event_schedule)       # content schedule

        article_suffix = u'<p>立即报名：<br>{0}<br> <p style="text-align: center;"><img src="{1}" max-width="600"> </p>'.format(
            event_url, event_suffix_pic)

        article_more = u'<p>更多<strong>{0}</strong>会议, 尽在活动家，欢迎使用活动家小程序查询报名会议，微信搜索“活动家会议”</p>'.format(
            event_tag_list)  # need tag_list

        article_content = article_prefix + article_event_content + article_suffix + article_more

        data = {
            "event_url": event_url,
            "event_id": event_id,
            "event_begin_time": event_begin_time,
            "event_end_time": event_end_time,
            "event_tag_list": event_tag_list,
            "article_title": article_title,  # 稿件标题
            "article_thumbnail": event_img_url,  # 缩略图地址
            "article_content": article_content,  # 要发送的文件内容
            "article_channel_id": self.channel_id,
            "article_category_id": self.category_id,
            "article_usercolumn_id": self.usercolumn_id,  # 分类id
        }

        return data

    def check_valid_url(self, link_list):
        """

        :param link_list:
        :return: a valid list
        """
        # TODO 读取log去重复
        # TODO 分页爬取

        log_name = self.create_log()

        with open(log_name, 'r') as rlog:
            check_list = rlog.readlines()  # need filter \n
            check_list = ["".join(line.strip()) for line in check_list]
            check_list = set(check_list)
            # print(check_list)
            rlog.close()

        valid_url_links = []
        del_link_list = []

        for target_url in link_list:
            if target_url in check_list:
                print("{0} had published!!!".format(target_url))
                del_link_list.append(target_url)

        for repeat_link in del_link_list:
            link_list.remove(repeat_link)
            # print(link_list)

        for target_url in link_list:
            valid_target_url = self.domain_url + target_url + "?json=1"
            valid_url_links.append(valid_target_url)

        ####
        # for target_url in link_list:
        #     while len(valid_url_links) < self.send_times:  # FIXME 大坑，如果valid_url_links < self.send_times, 会进入死循环, 目前解决方案，一次性读取足够多的link list, 分页遍历，先自定义一个范围.
        #         if target_url in check_list:
        #             print("{0} had published!!!".format(target_url))
        #             link_list.remove(target_url)
        #             print(link_list)
        #             break
        #         else:
        #             valid_target_url = self.domain_url + target_url + "?json=1"
        #             valid_url_links.append(valid_target_url)
        ###
        return valid_url_links

    def get_event_url_from_cat_url(self):
        """
        爬去网页，返回一个event_33333.html的不重复列表
        :return: link_list
        """
        # 获取网页内容
        r = requests.get(self.cat_url, headers=self.headers, timeout=10)
        print(self.cat_url)
        data = r.text

        link_list = re.findall(r"event-\d{10}.html", data)  # 页面匹配event-{old_event_id} 有3个重复

        # 加入遍历后面页面
        next_link_list = []
        for i in range(2, 7):
            cat_url = "https://www.huodongjia.com/{0}/page-{1}/".format(self.cat, i)
            # https://www.huodongjia.com/it/page-3/
            print("Next cat page visit cat url --->>>{0}".format(cat_url))
            r2 = requests.get(cat_url, headers=self.headers, timeout=10)
            link_list = re.findall(r"event-\d{10}.html", r2.text)
            next_link_list += link_list

        link_list = link_list + next_link_list
        all_link_list = set(link_list)  # 页面上匹配的link
        # print(all_link_list)
        return all_link_list

    def create_log(self):
        """
        create xxx.log for different account
        :return:
        """

        # print(os.getcwd())   # /Users/TesterCC/Development/python_workspace/Python_Network/mp_sohu_autosender
        # print(sys.path[0])   # /Users/TesterCC/Development/python_workspace/Python_Network/mp_sohu_autosender

        cat = 'all' if self.cat == "business" else self.cat  # business 对应 all 分类

        # file_name = os.getcwd() + '/' + cat + '.log'
        log_name = 'spider_' + cat + '.log'  # log_name format: spider_xx.log
        if os.path.exists(log_name):
            # print('文件{}已存在'.format(log_name))
            return log_name
        else:
            print('文件{}不存在，开始创建'.format(log_name))
            with open(log_name, 'at') as log:
                log.write('')
                log.close()
            print('文件{}已创建成功'.format(log_name))
            return log_name


if __name__ == '__main__':
    auto = AutoSender(username='18702895635')
    auto.login_platform()
    auto.send_article()
    auto.clear_account_cache()

    sleep(10)   # 建议不同账号间加上

    auto = AutoSender(username='15281005385')
    auto.login_platform()
    auto.send_article()
    auto.clear_account_cache()

    # 其他账号使用同上
