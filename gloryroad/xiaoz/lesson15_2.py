#coding:utf-8
'''
Created on 2016年3月16日

@author: PavilionLYX
'''

import urllib

#get   post
params=urllib.urlencode({'zz':18,'city':'Beijing'})
print params

#send get request
f = urllib.urlopen("http://python.org/query", params)
print f.getcode()
print f.geturl()

print "============================="

###接口测试可用
f2 = urllib.urlopen("http://python.org/query?%s" % params)
print f2.getcode()
print f2.geturl()
print f2.read()