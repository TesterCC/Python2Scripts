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


# non pic.huodongjia.com

URLS = ['http://img2.ctoutiao.com/uploads/2018/04/17/1523956754511321.jpg', 'http://5b0988e595225.cdn.sohucs.com/images/20180416/fbf4c2cf4ae444da84731aa9e44bbef9.jpeg']

TEXT = '<div style=\"padding: 0 10px\"><p>测试会议，请勿操作</p></div><p>就是这样测试1</p><p><img src=\"http://img2.ctoutiao.com/uploads/2018/04/17/1523956754511321.jpg"></p><p>就是这样测试2</p><p><img src=\"http://5b0988e595225.cdn.sohucs.com/images/20180416/fbf4c2cf4ae444da84731aa9e44bbef9.jpeg"></p>'

IMAGE_DOMAIN = 'https://pic.huodongjia.com/'

def convert_outside_urls(urls):
    '''
    @params urls: 外站图片URL list

    @rtype list:  返回活动家图片服务器  url list
    '''
    pool = ThreadPool(2)
    o = r'(http.+?\.jpg|http.+?\.png|http.+?\.bmp|http.+?\.gif|http.+?\.jpeg)'
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

    image = download_image_from_url(url)

    if image is None:
        return url

    try:
        # 得到活动家站内图片服务器图片URL
        t0 = time.time()
        print('costs begin............>>>>>>>>>>>>>>>>>>>>')
        # TODO insteaded by upload_file_by_http(url, image)
        inner_url = upload_file_by_http(url, image)
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
        image = requests.get(url, stream=True, timeout=5, verify=False)
        image_size = int(image.headers['content-length'])/1024
        if image_size > 1000:
            print('image size > 1M, do not download')
            return None
        print('finish fetch image URL........{}'.format(url))
        print('fetch image cost time : {}'.format(time.time() - start_time))
    except Timeout:
        logging.error('download outside url failed. caused by timeout')
        return None
    else:
        return image.content      #  return unicode


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


def upload_file_by_http(file_name, file_obj, directory='test-event-content'):
    '''
    use upyun sdk to upload file
    '''
    file_name = file_name.split('?')[0]

    BUCKETNAME = ''
    USERNAME = ''
    PASSWORD = ''

    up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30, endpoint=upyun.ED_AUTO)

    up.up_rest.endpoint = upyun.ED_AUTO

    sub_directory = datetime.date.strftime(datetime.date.today(),
                                           '%Y-%m-%d')
    server_directory = directory + '/' + sub_directory + '/'
    _, suffix = os.path.splitext(file_name)

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


