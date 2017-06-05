# -*- coding: utf-8 -*-
# !/usr/bin/env python

# http://www.imooc.com/video/13085
# https://developer.github.com/v3/users/

import json
import requests


URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    response = requests.get(build_uri('users/imoocdemo')) # get can replace with post,delete etc.
    print better_print(response.text)


def request_method_auth():
    response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'))
    print better_print(response.text)


def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print better_print(response.text)
    print response.request.headers
    print response.url

if __name__ == '__main__':
    # request_method()
    # print '==============================='
    # request_method_auth()
    params_request()