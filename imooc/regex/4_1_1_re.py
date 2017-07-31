#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10511
# python正则表达式之re模块方法介绍


import re

# search()
str1 = 'imooc videonum = 1000'

print(str1.find('1000'))   # 返回的是第一位匹配的索引

info = re.search(r'\d+', str1)
print(info.group())

print("---------------")

# findall()
str2 = 'c++=100, java=90, python=80'

info2 = re.search(r'\d+', str2)
print(info2.group())

info3 = re.findall(r'\d+', str2)
print(info3)     # return match value in a list

# total
total = sum(int(x) for x in info3)
print(total)