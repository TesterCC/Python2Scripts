# coding: utf-8
# http://cn.python-requests.org/zh_CN/latest/

import requests


r1 = requests.get('https://api.github.com/user', verify=False)
print "Status Code: %s " % r1.status_code
print "Response: %s" % r1.text
print "================================================"

r2 = requests.get('https://developer.github.com/v3', auth=('testerlyx@foxmail.com','-TesterCC07-'), verify=False)
print "Status Code: %s " % r2.status_code
# print "Response: %s" % r2.text
print "Content Type: %s" % r2.headers['content-type']
print "Encoding: %s" % r2.encoding
