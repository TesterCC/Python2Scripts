#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/20 09:22'

"""
for test upyun download by http
https://github.com/upyun/python-sdk
http://docs.upyun.com/api/rest_api/
http://docs.upyun.com/api/authorization/#header

curl -u eventpop:wert@123 http://v0.api.upyun.com/huodongjia-yun/
"""

import upyun
import requests
from requests.exceptions import Timeout

# config
BUCKETNAME = ''
USERNAME = ''
PASSWORD = ''

target_url = "http://img2.ctoutiao.com/uploads/2018/04/17/1523956754511321.jpg"

up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30, endpoint=upyun.ED_AUTO)

up.up_rest.endpoint = upyun.ED_AUTO

headers = { 'x-gmkerl-rotate': '180' }

# 数据流方式上传，可降低内存占用
# with open('mac_vim.jpg', 'rb') as f:
#     res = up.put('mav_vim2.png', f, checksum=True, headers=headers)
# print(res)

print('prepare fetch image URL........{}'.format(target_url))
image = requests.get(target_url, stream=True, timeout=5, verify=False)
image_size = int(image.headers['content-length']) / 1024
if image_size > 1000:
    print('image size > 1M, do not download')
print('finish fetch image URL........{}'.format(target_url))

print(type(image.content))          # 问题出在image这里，这的不是一个合法的image

r = up.put('/upyun-python-http/test.jpg', image.content)
print(r)

