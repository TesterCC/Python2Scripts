#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 接口测试基础之入门篇

import urllib
import urllib2

url = "http://xapi.kybyun.com/user/login"
headers = {}
headers = {
           'Host': 'xapi.kybyun.com',
           'Connection': 'keep-alive',
           'User-Agent': 'BangXueTang AipBot/1.0 (BangXueTang-IOS/2.1.3.1; IOS/9.30;iPhone 6 Plus)',
           'KY-UKEY': '940cd8dffd371d41eb0acbb7694fd5e9',
           'KY-SYSDEV': 'iPhone 6 Plus',
           'KY-SPEID': '1001010',
           'KY-SCHID': '1044',
           }
data = {}
data["appchg"] = 'AppStore'
data["apptype"] = '21'
data["appver"] = '2.1.3.1'
data["email"] = 'mushishi01'
data["isbind"] = '0'
data["passwd"] = '111111'
data["sysdev"] = 'iPhone 6 Plus'
data["sysver"] = '9.3'
data["uuid"] = '6ff7563dbd47c8077905c3920bc0d8b3'

# 数据编码以及赋值
data = urllib.urlencode(data)
req = urllib2.Request(url, data, headers)

# 打开地址并且赋值给变量
ResponseStr = urllib2.urlopen(req)

# 读取获得的值
ResponseStr = ResponseStr.read()

# 将获得的结果进行转码
ResponseStr = ResponseStr.decode("unicode_escape")
print(ResponseStr)
