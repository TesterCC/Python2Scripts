#!/usr/bin/env python
#coding=utf-8

# 3.文件属性及OS模块使用
# http://www.imooc.com/video/8043


import codecs


f = codecs.open('test.txt', 'w', 'utf-8')

print(f.encoding)

f.write(u"慕课")

f.close()

# cat test.txt

ff = open('test.txt', 'r+')
print(ff.read())
ff.close()