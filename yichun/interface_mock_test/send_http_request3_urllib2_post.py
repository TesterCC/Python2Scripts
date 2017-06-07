# coding:utf-8
"""
demo3 -- use urllib2 post
基础的，有鉴权则不能用
"""
import urllib2
import urllib
post_data = urllib.urlencode({}) 
response = urllib2.urlopen('http://192.168.2.141:8080/job/CheckPythonVersion/polling',post_data)
print response.read()
print response.getheaders()