#!/usr/bin/python
# coding:utf-8

# http://www.imooc.com/video/10682

import urllib2

# directly request
response = urllib2.urlopen('http://www.baidu.com')

# get status code, if return 200, means success.
print response.getcode()

# read content
cont = response.read()