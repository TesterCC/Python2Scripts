#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/10 13:36'

"""
高效开发 red book P232

教程用的Python2 Tonardo 4.3

本机环境Python2 Tonardo 5.0.2

同步I/O
"""

from tornado.httpclient import HTTPClient


def synchronous_visit():
    """
    同步I/O
    :return:
    """
    http_client = HTTPClient()
    response = http_client.fetch("http://www.baidu.com")
    print(response.body)


if __name__ == '__main__':
    synchronous_visit()
