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
admin website图片调试专用
"""
# non pic.huodongjia.com

# URLS = ['http://img2.ctoutiao.com/uploads/2018/04/17/1523956754511321.jpg', 'http://5b0988e595225.cdn.sohucs.com/images/20180416/fbf4c2cf4ae444da84731aa9e44bbef9.jpeg']

# add weixin url
#URLS = ['https://5b0988e595225.cdn.sohucs.com/images/20180427/ae379b3710da41c9942b42408b6f6711.jpeg', 'https://mmbiz.qpic.cn/mmbiz_jpg/HbibPwLYpapUlgE5KBibhibA9tO7sZseIanFycyiaSJYp6q5m7jBu0KQEmiaIwbIV1EEv8MAZjClSHokgsaIgI6TVlw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1', 'https://mmbiz.qpic.cn/mmbiz_gif/EKs3bvt0w0KUOKiaqaib6ibkVurv1PcLpyRZQSiaX57OFnr6EHA16sT5ks3VNn2B7GfrgNGNg4xtKibVtEa26JUPtRA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1', 'https://mmbiz.qpic.cn/mmbiz_png/EKs3bvt0w0KUOKiaqaib6ibkVurv1PcLpyRwYt7cuaj7byoK2muTYGvBribFgUxwWjwBiaDUY0N14wQmkjpt27ibzMyQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1']

# TODO
URLS = [u'https://mmbiz.qpic.cn/mmbiz_png/WFUq3GoJlzJCQdBeDLMUumE6rcBsEfVlWW9clXyUyTWJA0rryNjlV8K3C6iafQhmbNmQVL09gUPw9vZ5D5rkENA/640?wx_fmt=png&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1']

#URLS = [u'http://cdn.huodongxing.com/Content/v3.0/img/hdx/hdx-main-feature/admin-head/logo.png?auth_key=1529410900-0-0-0bbba0162ef76c08e31f21ec10841576', u'http://cdn.huodongxing.com/Content/v3.0/img/hdx/hdx-main-feature/admin-head/logo-fixed.png?auth_key=1529410900-0-0-aae3cf2befb8ceb059a560a4cf6b3c44', u'http://wimg.huodongxing.com/logo/201804/5437580567100/853084644198228_v2.jpg@!wmlogo?auth_key=1529410900-0-0-6450d839a4ad4ff39b4d11cd89154a56', u'http://cdn.huodongxing.com/logo/org/201507/8002023562675/762575473073460.jpg?auth_key=1529410900-0-0-dd9461f9af0b9c1bdcb919c83bc80fcb', u'http://cdn.huodongxing.com/Content/v2.0/img/vip/a1.png?auth_key=1529410900-0-0-2921469a2b00eb07054035842e9cb110', u'http://cdn.huodongxing.com/Content/v2.0/img/qr_normal.png?auth_key=1529410900-0-0-8eead9810ca6fd04dd19235b0717c7ca', u'http://cdn.huodongxing.com/file/20150717/1105CD0A15D687674FF1B692AB65BCB3A5/30493087821937393.jpg?auth_key=1529409933-0-0-e7185b6dc96d3987862f201b1fab303f', u'http://cdn.huodongxing.com/file/20150717/1105CD0A15D687674FF1B692AB65BCB3A5/30753065614871062.jpg?auth_key=1527593365-0-0-0a8c457041d49b51da35b8992ba791a2?auth_key=1527790550-0-0-4c7adb41e8d810bd61734c8d198de724?auth_key=1528801458-0-0-ac600ebf47eeed5e6e6df762f25bda10?auth_key=1528820757-0-0-ae82585f606ef8c274ca1df3cd3a29c6?auth_key=1528987843-0-0-bdcc5ebe21cc2ba93a13ce89b78739fb?auth_key=1529095380-0-0-d00d5f608fa3a15d4469ce3c693a2b70?auth_key=1529409933-0-0-9e82b5d78133dc9bd3365acda8478e8d', u'http://cdn.huodongxing.com/file/20150717/1105CD0A15D687674FF1B692AB65BCB3A5/30623065615121080.jpg?auth_key=1527593365-0-0-1cedd4afebe55471ac625b41c22cb3d1?auth_key=1527790550-0-0-cabd1fb4c4d943661e9ea42ae5f76c45?auth_key=1528801458-0-0-4c367ee7b886f6296b62a08058b96e59?auth_key=1528820757-0-0-e1a358c8e31df9fab3f09c0e30f87e65?auth_key=1528987843-0-0-995a06e54d3048bef9cb269cdc80614f?auth_key=1529095380-0-0-8f37b2a248f39d3af7f3dd5bbe505fe2?auth_key=1529409933-0-0-4725516a78ca94a4aa4928852fdbe4fa', u'http://cdn.huodongxing.com/file/20150717/1105CD0A15D687674FF1B692AB65BCB3A5/30913065615441113.jpg?auth_key=1527593365-0-0-8d193d06ce8e919a6876fe07a3340eaa?auth_key=1527593774-0-0-c9cc260b4772944b6c14e8eb0e1cbc9f?auth_key=1527790550-0-0-bd57d9e1637ffb19fd4d28176f8b34ef?auth_key=1528801458-0-0-3a36288677188469b8096d55e5ba6ca9?auth_key=1528820757-0-0-0294090075f68c36798003c2cadc786f?auth_key=1528987843-0-0-f038f838d9e53b9fbfdc8ed18a0a03f1?auth_key=1529095380-0-0-9d75fee834e41c41b80e50ef388cdd37?auth_key=1529409933-0-0-b6a0db15c21926a8fa0c15c7e51b0280', u'http://cdn.huodongxing.com/file/20150717/1105CD0A15D687674FF1B692AB65BCB3A5/30493065615781157.jpg?auth_key=1527593365-0-0-17760927f7fd8079288d90dfa6c5d662?auth_key=1527593774-0-0-a5175822baa5304640a2b12624ac1590?auth_key=1527790550-0-0-84ccba671e0a9c67ae69a85a2fa98f58?auth_key=1528801458-0-0-ec4f905a82843040d4f3fdeaa32f8e95?auth_key=1528820757-0-0-0b99e9f96e1a9ebed691dddc3d8dec3a?auth_key=1528987843-0-0-00bc0f78e2f20ce83626cf5e3ca88ac8?auth_key=1529095380-0-0-877e9d292bd84e98183950636caf909f?auth_key=1529409933-0-0-95c8e0e0edc3a408b3ef70c81b13c45a', u'http://cdn.huodongxing.com/file/20150717/1105CD0A15D687674FF1B692AB65BCB3A5/30663065615601130.jpg?auth_key=1527593365-0-0-c31d944bc2d1382181fe648e299fa723?auth_key=1527593774-0-0-6f10998806ac7f8bfe7f05cfb16a6286?auth_key=1527790550-0-0-f0801af69d0d0e0f80ea510c2183538e?auth_key=1528801458-0-0-34019df861b7ad3557a5ba8a6f6be235?auth_key=1528820757-0-0-8ba73ab00b67e7c5c0ec7a9e8dc8b735?auth_key=1528987843-0-0-144149f5787c6dc0a791fe513e1475be?auth_key=1529095380-0-0-0e9e253a7cdec9a998848fbad7479404?auth_key=1529409933-0-0-dc2c86bca27822ad2043a28c41f7fc96', u'http://cdn.huodongxing.com/Content/v2.0/img/face/male/11.jpg?auth_key=1529410900-0-0-1051837066fbd3c0a09e8be3c1053655', u'http://cdn.huodongxing.com/Content/v2.0/img/face/male/11.jpg?auth_key=1529410900-0-0-1051837066fbd3c0a09e8be3c1053655', u'http://cdn.huodongxing.com/Content/v2.0/img/face/female/8.jpg?auth_key=1529410900-0-0-24d3d270e21cbc2ff91ab0ad93a42e32', u'http://cdn.huodongxing.com/Content/v2.0/img/face/female/42.jpg?auth_key=1529410900-0-0-b368d2d8cf6f345171588f5861a45160', u'http://cdn.huodongxing.com/Content/v2.0/img/face/male/15.jpg?auth_key=1529410900-0-0-909323aaafa3bc267b159ece8f42345a', u'http://cdn.huodongxing.com/Content/v2.0/img/face/male/13.jpg?auth_key=1529410900-0-0-721371339c7e292ac80afaf4e1ccef21', u'http://cdn.huodongxing.com/logo/201806/8444912964200/643089725446764_v2small.jpg?auth_key=1529410900-0-0-e4f98ba721a9dcb2033baa94e5bff03b', u'http://cdn.huodongxing.com/logo/201801/6422321822900/662932796683773_v2small.jpg?auth_key=1529410900-0-0-1a0fd8e5e3417254d38fb234b789514f', u'http://cdn.huodongxing.com/logo/201806/3443027130000/783077626053090_v2small.jpg?auth_key=1529410900-0-0-ed928a1490ed86af769dc8b37a433449', u'http://cdn.huodongxing.com/logo/201804/4434250388500/993015633108725_v2small.jpg?auth_key=1529410900-0-0-4c851945ec25a5d07493ae762cefcc71', u'http://cdn.huodongxing.com/logo/201801/5423455943200/412940683620196_v2small.jpg?auth_key=1529410900-0-0-a5d4d6cd1a53b0902f43b323d2799909', u'http://cdn.huodongxing.com/logo/201806/2444204266300/743084752635975_v2small.jpg?auth_key=1529410900-0-0-9a823f7a5972a5c7dba9dc60b1f0e061', u'http://cdn.huodongxing.com/logo/201805/3439113572900/553049412910428_v2small.jpg?auth_key=1529410900-0-0-2957eddb338baf60fc93e4d4b787e0cb', u'http://cdn.huodongxing.com/logo/201806/4444453541200/843086483184155_v2small.jpg?auth_key=1529410900-0-0-2a95c48b8b2c1542b163c6770682d7d1', u'http://cdn.huodongxing.com/Content/app/appom/422671633331741.jpg', u'http://cdn.huodongxing.com/Content/img/mark1.png?auth_key=1529410900-0-0-b14fa8a85b6a48b28ad6e3f679e38613', u'http://cdn.huodongxing.com/logo/org/201507/8002023562675/762575473073460.jpg?auth_key=1529410900-0-0-dd9461f9af0b9c1bdcb919c83bc80fcb', u'http://cdn.huodongxing.com/Content/v2.0/img/vip/a1.png?auth_key=1529410900-0-0-2921469a2b00eb07054035842e9cb110']
print(len(URLS))

# URLS = ['http://img2.hudongba.com/upload/_oss/uePasteUpload/201806/1511/1529034655756.jpg', 'http://img2.hudongba.com/upload/_oss/uePasteUpload/201806/1511/1529034655801.jpg']


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
    # current
    o = r'(http.+?\.jpg|http.+?\.png|http.+?\.bmp|http.+?\.gif|http.+?\.jpeg|https:\/\/mmbiz.qpic.cn\/mmbiz_(?:jpg|gif|png|jpeg)\/.+?\/)'

    # abort
    # o = r'(http.+?\.jpg|http.+?\.png|http.+?\.bmp|http.+?\.gif|http.+?\.jpeg|https:\/\/mmbiz.qpic.cn\/mmbiz_(?:jpg|gif|png|jpeg)\/.+?wx_fmt.+?&)'   # with wx_fmt=png


    try:
        img_urls = [re.findall(o, u)[0] for u in urls]
    except IndexError as e:
        # 没有匹配到图片URL，此时不作处理
        # FIXME 这里实际上可以优化为  外站图片符合规则，则上传， 否则用原图，不作上传处理
        # print(e)
        print(traceback.format_exc())
        return urls

    replace_url_list = pool.map(lambda url: _convert_url(url), img_urls)
    pool.close()
    pool.join()
    print("Finish convert url >>> {}".format(replace_url_list))
    print(len(urls))
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
        if image_type in ["png", "jpeg", "jpg", "gif", "bmp", "octet-stream", "webp"]:
            image_size = int(image.headers['content-length'])/1024
            if image_size > 2000:
                print('image size > 2M, do not download')
                return None    # FIXME 不能用这个，否则index error, 但是干掉又会下载图片使大小check无效
            print('finish fetch image URL........{}'.format(url))
            print('fetch image cost time : {}'.format(time.time() - start_time))
        else:
            print('image_type is error, current type : {}'.format(image_type))
            return None  # return None时会引起index error,导致转换失败
    except Timeout:
        logging.error('download outside url failed. caused by timeout')
        print(traceback.format_exc())
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


