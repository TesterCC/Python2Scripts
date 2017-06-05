# coding:utf-8
# !/usr/bin/env python

# http://www.imooc.com/video/13091

import requests


target_url = 'https://api.github.com'
# target_url = 'https://www.baidu.com'

def get_key_info(response,*args,**kwargs):
    """
    回调函数
    :return:
    """
    print response.headers['Content-Type']


def main():
    """
    main programming
    """
    requests.get(target_url, hooks=dict(response=get_key_info))


main()