#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10510
# 分组匹配


import re


ma = re.match(r'abc|d', 'abc')

ma2 = re.match(r'abc|d', 'ddd')

print(ma.group())
print(ma2.group())
print("---------------------------")

#  匹配0-100间任意一个数字组成的字符串
m1 = re.match(r'[1-9]?\d$', '9')
print(m1.group())

m2 = re.match(r'[1-9]?\d$', '99')
print(m2.group())

# m3 = re.match(r'[1-9]?\d$', '09')    # faild
# print(m3.group())

m4 = re.match(r'[1-9]?\d$|100', '100')
print(m4.group())

print("---------------------------")

m5 = re.match(r'[\w]{4,6}@163.com', 'immoc@163.com')
print(m5.group())

m6 = re.match(r'[\w]{4,6}@(163|126).com', 'immoc@126.com')
print(m6.group())