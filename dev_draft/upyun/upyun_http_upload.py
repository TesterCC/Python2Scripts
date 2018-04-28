#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/20 09:22'

"""
for test upyun download by http
https://github.com/upyun/python-sdk
http://docs.upyun.com/api/rest_api/
http://docs.upyun.com/api/authorization/#header

curl -u USERNAME:PASSWORD http://v0.api.upyun.com/huodongjia-yun/
BUCKETNAME = 'huodongjia-yun'

https://note.youdao.com/web/#/file/WEBef88c0b328111992bc7fb37aa742c187/note/WEBea03e1d3f6e046bed3484906e9aa6c60/

integrated test
"""

import os
import time
import datetime
import upyun
import requests
from requests.exceptions import Timeout

# config
BUCKETNAME = ''
USERNAME = ''
PASSWORD = ''

PIC_DOMAIN = 'https://pic.huodongjia.com'

target_url = "http://img2.ctoutiao.com/uploads/2018/04/17/1523956754511321.jpg"
# target_url = "https://mmbiz.qpic.cn/mmbiz_jpg/EKs3bvt0w0KUOKiaqaib6ibkVurv1PcLpyR6StUYKLt5Lcm7bhyFJFuiaBXOWadGWBgaF84yTSIQF7b9NdmI6bxnnw/640?wx_fmt=jpeg&"
# target_url = "https://mmbiz.qpic.cn/mmbiz_jpg/HbibPwLYpapUlgE5KBibhibA9tO7sZseIanFycyiaSJYp6q5m7jBu0KQEmiaIwbIV1EEv8MAZjClSHokgsaIgI6TVlw/640?wx_fmt=jpeg&"
# target_url = "https://mmbiz.qpic.cn/mmbiz_gif/EKs3bvt0w0KUOKiaqaib6ibkVurv1PcLpyRZQSiaX57OFnr6EHA16sT5ks3VNn2B7GfrgNGNg4xtKibVtEa26JUPtRA/640?wx_fmt=gif&"

# target_url = "https://mmbiz.qpic.cn/mmbiz_jpg/HbibPwLYpapWGjuQ1R7SficQa3hEicDdQicoLNQcibyaDdiaZDGF6QoZ9cWe8iboSCoqwlbdODjOmmLgrxGYiaBVIl99VA/"

# regex filter


up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30, endpoint=upyun.ED_AUTO)

up.up_rest.endpoint = upyun.ED_AUTO

headers = { 'x-gmkerl-rotate': '180' }

# 数据流方式上传，可降低内存占用
# with open('mac_vim.jpg', 'rb') as f:
#     res = up.put('mav_vim2.png', f, checksum=True, headers=headers)
# print(res)

print('prepare fetch image URL........{}'.format(target_url))
image = requests.get(target_url, stream=True, timeout=5, verify=False)

print("will download images type:")
image_type = image.headers['Content-Type'].split('/')[-1]
print(image.headers['Content-Type'])
print(image_type)

print("*" * 30)

image_size = int(image.headers['content-length']) / 1024
if image_size > 1000:
    print('image size > 1M, do not download')
print('finish fetch image URL........{}'.format(target_url))

print(type(image.content))



# upload_path
# sub_directory = datetime.date.strftime(datetime.date.today(), '%Y-%m-%d')

# directory = 'event-content'

# server_directory = directory + '/' + sub_directory + '/'
# _, suffix = os.path.splitext(file_name)

# focus on wx image
# suffix = target_url.split("wx_fmt=")
#
# suffix = suffix[-1].replace("&", "")
# print(suffix)


upload_time = time.time()
# r = up.put('/upyun-python-http/test_{}.{}'.format(upload_time, suffix), image.content)
r = up.put('/upyun-python-http/test_{}'.format(upload_time), image.content)
print(r)

# 微信公众号的图片 {'frames': '1', 'width': '1080', 'file-type': 'WEBP', 'created-date': 'Sat, 28 Apr 2018 01:56:00 GMT', 'height': '608'}
# 只有chrome能正常访问

# visit_upload_url = PIC_DOMAIN + '/upyun-python-http/test_{}.{}'.format(upload_time, suffix)
visit_upload_url = PIC_DOMAIN + '/upyun-python-http/test_{}'.format(upload_time)
print(visit_upload_url)



