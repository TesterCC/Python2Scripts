#coding:utf-8

'''
Created on 2016年3月16日

@author: PavilionLYX
'''

import urllib,urllib2
import base64

url=r'https://www.baidu.com/'
base64string=base64.encodestring('落地的大白菜:ldddbc').strip() #生成空白符，这里是生成换行符
authheader="Basic "+base64string
req=urllib2.Request(url)
req.add_header('Authorization', authheader)
fp=urllib2.urlopen(req)
print fp.info()
print fp.getcode()
print fp.geturl()
print fp.read()


