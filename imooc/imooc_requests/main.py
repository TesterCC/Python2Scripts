# !/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.imooc.com/video/13085
# http://www.imooc.com/video/13087
# http://www.imooc.com/video/13088
# https://github.com/jian-en/imooc-requests.git
# https://developer.github.com/v3/users/


import json
import requests
from requests import exceptions


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


def json_request():
    response = requests.patch(build_uri('user'), auth=('imoocdemo','imoocdemo123'), json={'name': 'babymooc2', 'email': 'hello-world@imooc.org'})
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code


def json_request2():
    response = requests.post(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), json=['test@github.com'])
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code


def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'),timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print response.text
        print response.status_code


def hard_requests():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'fake0.0.1'}
    req = Request('GET',build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),headers=headers)
    prepped = req.prepare()
    print prepped.body
    print prepped.headers

    resp = s.send(prepped, timeout=5)
    print resp.status_code
    print resp.request.headers
    print resp.text

if __name__ == '__main__':
    # request_method()
    # print '==============================='
    # request_method_auth()
    # params_request()
    # json_request()
    # json_request2()
    # timeout_request()
    hard_requests()