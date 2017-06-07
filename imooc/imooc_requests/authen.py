# coding:utf-8
# !/usr/bin/env python

import requests
import base64

BASE_URL = 'https://api.github.com'


def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])


def basic_auth():
    """
    基本认证
    """
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print response.text
    print response.request.headers

basic_auth()

print "User&Password:",
print base64.b64decode('aW1vb2NkZW1vOmltb29jZGVtbzEyMw==')