#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10511
# python正则表达式之re模块方法介绍


import re

# sub()
str3 = 'imooc videonum = 9999'
info = re.sub(r'\d+', '1001', str3)      # 不加count的话默认都替换
print(info)


def add1(match):
    val = match.group()
    num = int(val)+1
    return str(num)

info2 = re.sub(r"\d+", add1, str3)
print(info2)


# split()

str4 = 'imooc:C C++ Java Python Go PHP,Ruby'
info4 = re.split(r":| |,", str4)    # 这里匹配的是冒号或空格或逗号，都是英文符号
print(info4)