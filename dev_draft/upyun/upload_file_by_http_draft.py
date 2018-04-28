#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/20 13:31'


from multiprocessing.dummy import Pool as ThreadPool
import re
import time
import traceback
import logging
import datetime
import random
import os

import requests
from requests.exceptions import Timeout
import upyun


"""
https://note.youdao.com/web/#/file/WEBef88c0b328111992bc7fb37aa742c187/note/WEBea03e1d3f6e046bed3484906e9aa6c60/
"""
# non pic.huodongjia.com

# URLS = ['http://img2.ctoutiao.com/uploads/2018/04/17/1523956754511321.jpg', 'http://5b0988e595225.cdn.sohucs.com/images/20180416/fbf4c2cf4ae444da84731aa9e44bbef9.jpeg']

# add weixin url
URLS = ['https://5b0988e595225.cdn.sohucs.com/images/20180427/ae379b3710da41c9942b42408b6f6711.jpeg', 'https://mmbiz.qpic.cn/mmbiz_jpg/HbibPwLYpapUlgE5KBibhibA9tO7sZseIanFycyiaSJYp6q5m7jBu0KQEmiaIwbIV1EEv8MAZjClSHokgsaIgI6TVlw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1', 'https://mmbiz.qpic.cn/mmbiz_gif/EKs3bvt0w0KUOKiaqaib6ibkVurv1PcLpyRZQSiaX57OFnr6EHA16sT5ks3VNn2B7GfrgNGNg4xtKibVtEa26JUPtRA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1', 'https://mmbiz.qpic.cn/mmbiz_png/EKs3bvt0w0KUOKiaqaib6ibkVurv1PcLpyRwYt7cuaj7byoK2muTYGvBribFgUxwWjwBiaDUY0N14wQmkjpt27ibzMyQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1']

# TEXT = '<div style=\"padding: 0 10px\"><p>测试会议，请勿操作</p></div><p>就是这样测试1</p><p><img src=\"http://img2.ctoutiao.com/uploads/2018/04/17/1523956754511321.jpg"></p><p>就是这样测试2</p><p><img src=\"http://5b0988e595225.cdn.sohucs.com/images/20180416/fbf4c2cf4ae444da84731aa9e44bbef9.jpeg"></p>'

IMAGE_DOMAIN = 'https://pic.huodongjia.com/'

def convert_outside_urls(urls):
    '''
    @params urls: 外站图片URL list

    @rtype list:  返回活动家图片服务器  url list
    '''
    pool = ThreadPool(4)
    # o = r'(http.+?\.jpg|http.+?\.png|http.+?\.bmp|http.+?\.gif|http.+?\.jpeg)'   # normal one

    # get weixin url, but need to deal with weixin image suffix
    o = r'(http.+?\.jpg|http.+?\.png|http.+?\.bmp|http.+?\.gif|http.+?\.jpeg|https:\/\/mmbiz.qpic.cn\/mmbiz_(?:jpg|gif|png|jpeg)\/.+?\/)'

    # o = r'(http.+?\.jpg|http.+?\.png|http.+?\.bmp|http.+?\.gif|http.+?\.jpeg|https:\/\/mmbiz.qpic.cn\/mmbiz_(?:jpg|gif|png|jpeg)\/.+?wx_fmt.+?&)'   # with wx_fmt=png

    print(urls)
    try:
        img_urls = [re.findall(o, u)[0] for u in urls]
    except IndexError:
        # 没有匹配到图片URL，此时不作处理
        # FIXME 这里实际上可以优化为  外站图片符合规则，则上传， 否则用原图，不作上传处理
        return urls

    replace_url_list = pool.map(lambda url: _convert_url(url), img_urls)
    pool.close()
    pool.join()
    print("Finish convert url >>> {}".format(replace_url_list))
    return replace_url_list


def _convert_url(url):
    if not url.startswith(('http', 'https')):
        return ''

    # image = download_image_from_url(url)

    image, image_type = download_image_from_url(url)   # return image_tye

    if image is None:
        return url

    try:
        # 得到活动家站内图片服务器图片URL
        t0 = time.time()
        print('costs begin............>>>>>>>>>>>>>>>>>>>>')
        # TODO insteaded by upload_file_by_http(url, image)
        inner_url = upload_file_by_http(image, image_type)
        print('costs {}'.format(time.time() - t0))
    except:
        logging.error(traceback.format_exc())
        print(traceback.format_exc())
        return url
    else:
        return inner_url


def download_image_from_url(url):
    '''
    访问外部图片， 返回 file obj
    '''
    try:
        start_time = time.time()
        # print('prepare fetch image URL........{}'.format(url))
        image = requests.get(url, stream=True, timeout=7, verify=False)

        # debug
        # print("will download images type:")
        image_type = image.headers['Content-Type'].split('/')[-1]
        # print(image_type)
        # print(type(image_type))
        # print(image.headers['Content-Type'])
        if image_type in ["png", "jpeg", "jpg", "gif", "bmp"]:
            image_size = int(image.headers['content-length'])/1024
            if image_size > 1000:
                print('image size > 1M, do not download')
                return None
            print('finish fetch image URL........{}'.format(url))
            print('fetch image cost time : {}'.format(time.time() - start_time))
        else:
            print('image_type is error, current type : {}'.format(image_type))
            return None
    except Timeout:
        logging.error('download outside url failed. caused by timeout')
        return None
    else:
        return image.content, image_type      #  return unicode


def multi_sub(replace_url_list, text):
    '''
    将文本中包含这些URL的，替换成新的URL(replace_url_list)
    https://stackoverflow.com/questions/764360/a-list-of-string-replacements-in-python
    '''
    image_regex = re.compile(
        r'<img .*?src="(?!https?://pic\.huodongjia\.com)(.*?)".*?>')

    # 由于re.sub是整个匹配，所以需要取分组, 只替换 src 中间的东西，有没有更好的方法呢~
    # self.sub_image_regex = re.compile(r'(<img .*src=")(?!https?://pic\.huodongjia\.com)(.*?)(".*?>)')  # error
    sub_image_regex = re.compile(r'(<img .*?src=")(?!https?:\/\/pic\.huodongjia\.com)([^"]*)(".*?>)')
    return sub_image_regex.sub(
        lambda i: i.group(1) + replace_url_list.pop(0) + i.group(3),
        text)


def upload_file_by_http(file_obj, image_type, directory='test-event-content'):
    '''
    use upyun sdk to upload file
    '''

    BUCKETNAME = ''
    USERNAME = ''
    PASSWORD = ''

    up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30, endpoint=upyun.ED_AUTO)

    up.up_rest.endpoint = upyun.ED_AUTO

    sub_directory = datetime.date.strftime(datetime.date.today(),
                                           '%Y-%m-%d')
    server_directory = directory + '/' + sub_directory + '/'

    print("sub_directory: {}".format(sub_directory))

    # _, suffix = os.path.splitext(file_name)
    suffix = "." + image_type

    # print("suffix is: {}".format(suffix))

    print("Server directory is {}".format(server_directory))

    upload_filename = str(time.time()) + str(random.randint(0, 9999)) + suffix

    try:
        up.put(server_directory + upload_filename, file_obj)
    except upyun.UpYunServiceException as se:
        print('Except an UpYunServiceException ...')
        print('Request Id: ' + se.request_id)
        print('HTTP Status Code: ' + str(se.status))
        print('Error Message:    ' + se.msg + '\n')
    except upyun.UpYunClientException as ce:
        print('Except an UpYunClientException ...')
        print('Error Message: ' + ce.msg + '\n')
    else:
        # print(IMAGE_DOMAIN + server_directory + upload_filename)
        return IMAGE_DOMAIN + server_directory + upload_filename


if __name__ == '__main__':
    convert_outside_urls(URLS)


