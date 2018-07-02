#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/23 04:24'

import requests
import json

# 测试下Python的兼容性

access_token = "11_4LXEASFtFR4AUJCNWyEcQ2-7cl3qgFmMnc4RU3ZjSWyOjGSj7i0b1Eksj37QF48S4zR12WSeCJWomA7r49z12EhP15_1ZPo2-kUqttZmbwr-zWXHK5s6wdGlFRbshDqTa70z1nKfqAFPpDvFLREiAHAPVI"

url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(access_token)

content = u'''Python2欢迎关注活动家——国内会议查询报名第一平台\n\n一键查询近期热门会议信息，试试回复：区块链\n\n马上开启大咖之旅，从<a href="https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA4NjEzNTYxMw==&scene=124#wechat_redirect">点击这里开始</a>'''
# content = u'<a href="http://www.qq.com">点击跳小程序</a>'

data = {
    "touser": "oPbHyt4UFfQdOANBjVfjmGWaJZOo",  # user openid
    "msgtype": "text",
    "text": {
        "content": content,
    }
}

# 这两步处理很关键，否则微信会回复/uXXXX
# 注意和Python3的区别
data = json.dumps(data, ensure_ascii=False)    # unicode
print(type(data))

# data2 = json.dumps(data)    # str
# print(type(data2))


data = data.encode('utf-8')    # str

ret = requests.post(url, data=data)

print(ret.text)
