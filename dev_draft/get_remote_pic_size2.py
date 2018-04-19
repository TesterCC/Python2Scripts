#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/18 16:13'

import logging

import requests
from requests.exceptions import Timeout

"""
Python快速获取图片文件大小

https://www.v2ex.com/t/67865
https://blog.csdn.net/pud_zha/article/details/8809878
HTTP之Content-Length
"""

log = logging.getLogger('website.debug')
# URL = 'https://pic.huodongjia.com/event/2017-12-20/1513755021.78.jpg'
# URL = 'https://pic.huodongjia.com/event/2018-02-23/1519357566.95.jpg'   # can pass
URL ='http://lensbuyersguide.com/gallery/219/2/23_iso100_14mm.jpg'    # > 5M, failed


def check_download_img_from_url(url=URL):
    # 两种写法都可用
    try:
        # pre_img_size = requests.head(url).headers.get('content-length')   # content-length单位为字节
        image = requests.get(url, stream=True, timeout=5, verify=True)
        image_size = int(image.headers['content-length'])/1024

        print("{} k".format(image_size))   # 1343024字节/1024

        if image_size > 1000:
            print("image size > 1M, do not download")
            log.debug("")
            return None
    except Timeout:
        log.error('download outside url failed. caused by timeout')
        return None
    else:
        print("符合要求可以正常开始下载")
        return image.raw


if __name__ == '__main__':
    rt = check_download_img_from_url()
    print(type(rt))



