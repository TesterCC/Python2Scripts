#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10509
# 匹配模式变为非贪婪模式


import re

# 非贪婪模式
ma = re.match(r'[0-9][a-z]*?', '1bc')

ma2 = re.match(r'[0-9][a-z]*', '1bc')    # 贪婪模式

ma3 = re.match(r'[0-9][a-z]+?', '1bc')

ma4 = re.match(r'[0-9][a-z]??', '1bc')

print("非贪婪模式")
print(ma.group())
print(ma3.group())
print(ma4.group())
print("------------------")
print("贪婪模式")
print(ma2.group())
