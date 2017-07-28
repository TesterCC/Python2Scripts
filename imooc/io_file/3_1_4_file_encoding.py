#!/usr/bin/env python
#coding=utf-8

# 3.文件属性及OS模块使用
# http://www.imooc.com/video/8043


import os


f = open("imooc0.txt", "r+")

print(f.read())

# f.write('123')
# f.write(u"慕课")    # 会报错ascii codec不能直接写入unicode字符

a = unicode.encode(u"慕课", 'utf-8')

print(a)
f.write(a)
f.seek(0, os.SEEK_SET)

print(f.read())