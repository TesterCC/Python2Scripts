# !/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.imooc.com/video/13084

import requests

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'


def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Response Body:'
    print response.text


def uss_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    # send request
    response = requests.get(URL_IP, params=params)
    # handle response
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Status Code:'
    print response.status_code, response.reason
    print '>>>>Response Body:'
    print response.json()


if __name__ == '__main__':
    print '>>> Use simple requests:'
    use_simple_requests()
    print '================================='
    print '>>> Use params requests:'
    uss_params_requests()