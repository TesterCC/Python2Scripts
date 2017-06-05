# coding:utf-8
# !/usr/bin/env python

# http://bblove.me/2015/05/23/python-requests-login-csdn-blog/

import requests

r = requests.get('http://www.baidu.com')
print r.text
