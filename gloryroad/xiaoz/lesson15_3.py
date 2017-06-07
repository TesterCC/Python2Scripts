#coding:utf-8
'''
Created on 2016年3月16日

@author: PavilionLYX
'''

import urllib
import urlparse

url3 = r'http://www.baidu.com/user/index.html;20?name=zz&age=18!#8888'

res=urlparse.urlparse(url3)

print res

print res[0]

print res[1]

print res[2]