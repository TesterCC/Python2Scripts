#!/usr/bin/python
# coding:utf-8

# http://www.imooc.com/video/10683  http://www.imooc.com/learn/563

import urllib2
import cookielib

url = "http://www.baidu.com"

print "First Method"
# directly request
response1 = urllib2.urlopen(url)

# get status code, if return 200, means success.
print response1.getcode()

# read content
cont = response1.read()
print len(cont)

print "=============================================="
print "Second Method"

request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "=============================================="
print "Third Method"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print "------------------------------------"
print response3.read()




