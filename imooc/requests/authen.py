# coding:utf-8
# !/usr/bin/env python

# http://www.imooc.com/video/13092

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


def basic_oauth():
    headers = {'Authorization': 'token a0f7d996f1468ab0c397e2114554dc37e2d4e20e'}

    # user/emails
    response = requests.get(construct_url('user/emails'), headers=headers)
    print response.request.headers
    print response.text
    print response.status_code


from requests.auth import AuthBase


class GithubAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        # requests add headers
        r.headers['Authorization'] = ' '.join(['token', self.token])  # space is separator
        return r


def oauth_advanced():
    auth = GithubAuth('a0f7d996f1468ab0c397e2114554dc37e2d4e20e')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print response.text
    print response.status_code

# basic_auth()

# print "User&Password:",
# print base64.b64decode('aW1vb2NkZW1vOmltb29jZGVtbzEyMw==')

# basic_oauth()

oauth_advanced()
