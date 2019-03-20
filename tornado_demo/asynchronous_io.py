#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/10 14:21'

"""
高效开发 red book红书 P232

教程用的Python2 Tonardo 4.3   
workon testvir

本机环境Python2 Tonardo 5.0.2  # 用法不一样了

异步I/O
"""

from tornado.httpclient import AsyncHTTPClient


def handle_response(response):
    print(response.body)

def asynchronous_visit():
    http_client = AsyncHTTPClient()
    http_client.fetch("http://xueshu.baidu.com", callback=handle_response)  # 函数会在调用后立刻返回而无须等待实际完成

if __name__ == '__main__':
    asynchronous_visit()