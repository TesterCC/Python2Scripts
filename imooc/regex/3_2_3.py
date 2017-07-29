#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10509
# 匹配0-99之间任意一个数字


import re


ma = re.match(r'[1-9]?[0-9]', '99')      # ? 匹配前一个字符0次或1次
ma3 = re.match(r'[1-9]?[0-9]', '1')      # ? 匹配前一个字符0次或1次
ma4 = re.match(r'[1-9]?[0-9]', '09')      # ? 匹配前一个字符0次或1次

print(ma.group())
print(ma3.group())
print(ma4.group())
print("-------------------")

# {m,n}

ma0 = re.match(r'[a-zA-Z0-9]{6}', 'abc123')
# ma0 = re.match(r'[a-zA-Z0-9]{6}', 'abc12345')   # return abc123
# ma0 = re.match(r'[a-zA-Z0-9]{6}', 'abc12_')   #  failed
print(ma0.group())


ma5 = re.match(r'[a-zA-Z0-9]{6}@163.com', 'abc123@163.com')
print(ma5.group())
print("-------------------")

# 指定匹配次数6到10次
ma6 = re.match(r'[a-zA-Z0-9]{6,10}@163.com', 'abc123456@163.com')
print(ma6.group())




