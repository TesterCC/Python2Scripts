#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10510
# \<number> 引用编号为num的分组匹配到的字符串

# match xml

import re

ma = re.match(r'<[\w]+>', "<book>")
print(ma.group())

ma2 = re.match(r'<([\w]+>)', "<book>")
print(ma2.group())

ma3 = re.match(r'<([\w]+>)', "<book>")
print(ma3.groups())

ma4 = re.match(r'<([\w]+>)\1', "<book>book>")
print(ma4.group())

ma5 = re.match(r'<([\w]+>)[\w]+</\1', "<book>python</book>")
print(ma5.group())

ma6 = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', "<book>python</book>")    # use (?P=mark) isntead of \1
print(ma6.group())
