#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/10/17 15:52'

# -*- coding:utf-8 -*-
import json
import requests

import logging

log = logging.getLogger('website.debug')


def send_email_by_sendcloud(sub, content, to, from_email=None, from_name=None, tag_id=None):
    '''
    调用sendcloud接口，发送邮件
    '''
    ret = {}
    url = "http://sendcloud.sohu.com/webapi/mail.send.json"
    API_USER = ''
    API_KEY = ''

    # 配置各项参数
    params = {
        "api_user": API_USER,  # 使用api_user和api_key进行验证
        "api_key": API_KEY,
        "from": from_email if from_email else 'test@test.com',  # 发信人, 用正确邮件地址替代
        "fromname": from_name if from_name else u'xxx团队',  # 邮件来源
        "to": ';'.join(to),  # 收件人地址列表
        "subject": sub.encode('utf-8'),  # 主题
        "html": content.encode('utf-8'),  # 邮件内容
        "resp_email_id": "true",
        "label": int(tag_id) if tag_id else None,  # 标签id
    }

    # 调用接口，执行发送
    try:
        resp = requests.post(url, data=params)
        result = resp.json()
        if result['message'] == 'success':
            ret['code'] = 1
            ret['message'] = 'success'
        else:
            ret['code'] = 0
            ret['message'] = 'failed'
    except Exception, e:
        ret['code'] = 0
        ret['message'] = 'failed'
        log.debug('******调用sendcloud出错********')
        log.debug(e)

    return ret


if __name__ == '__main__':
    # kwargs = {
    #     'to': ['1791935171@qq.com'],
    #     'sub': u'活动家Python开发',
    #     'content': u'<html><body>活动家test，全球最大的会议平台, 测试标签2</body></html>',
    #     'tag_id': 7134
    # }

    kwargs = {
        'to': ['xxxxx@qq.com'],
        'sub': u'Python开发',
        'content': u'<html><body>test，XX平台, 测试</body></html>'
    }
    print send_email_by_sendcloud(**kwargs)