#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10510


import re

# 从0开始匹配，但是如果0就匹配失败就返回None
ma = re.match('[\w]{4,10}@163.com', 'imooc@163.com')
print(ma.group())

ma2 = re.match('[\w]{4,10}@163.com', 'imooc@163.com33')
print(ma2.group())

ma3 = re.match(r'^[\w]{4,10}@163.com$', 'imooc@163.com')
print(ma3.group())    # use ^ $

print("----------------------")

# use \A \Z
ma4 = re.match(r'\Aimooc[\w]*', 'imoocpython')
print(ma4.group())
