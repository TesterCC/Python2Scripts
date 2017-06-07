# coding:utf-8
"""
demo2 -- use urllib2 get
"""

import urllib2
response = urllib2.urlopen("http://192.168.2.141:8080/api/json?pretty=true")
print response.read()