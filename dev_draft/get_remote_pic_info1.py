#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/17 23:11'


import cStringIO, urllib2
from PIL import Image

"""
python获取远程图片大小和尺寸的方法 in Python2
python获取图片尺寸大小
通过urllib2打开远程图片，通过cStringIO读取文件内容，不用保存到磁盘即可读取图片文件的信息
"""

url = 'https://pic.huodongjia.com/event/2017-12-20/1513755021.78.jpg'

file = urllib2.urlopen(url)
print(file)
print(type(file))

tmp = cStringIO.StringIO(file.read())
im = Image.open(tmp)

print(im.format)
print(im.size)
print(im.mode)
