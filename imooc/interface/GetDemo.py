#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
http://www.imooc.com/video/13104
接口测试基础之入门篇
yx07
'''

import urllib
import urllib2

url = "http://reg.haibian.com/login/ajax_login"

# 定义请求数据，并且对数据进行赋值
data = {}
data["loginnae"] = 'student08@qq.com'
data["password"] = '96e79218965eb72c92a549dd5a330112'
# md5: 	96e79218965eb72c92a549dd5a330112

# 对请求数据进行编码
data = urllib.urlencode(data)

# 将数据和url进行连接
request = url+'?'+data

# 打开请求，获取对象
requestResponse = urllib2.urlopen(request)

# 读取服务端返回的数据
ResponseStr = requestResponse.read()
ResponseStr2 = ResponseStr.decode("unicode_escape")

#打印数据
print(ResponseStr2)

