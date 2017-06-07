#!/usr/bin/env python
#coding=utf-8

# http://www.imooc.com/learn/550
# http://www.imooc.com/video/10508   匹配单个字符

import re

ma = re.match(r'a', 'a')  # match char, all text

print type(ma)
print ma.group()

ma2 = re.match(r'a', 'b')
print type(ma2)


ma3 = re.match(r'.', 'b')
print type(ma3)
print ma3.group()

ma4 = re.match(r'.', '0')   # . 匹配任意一个字符， ..匹配任意两个字符
print type(ma4)
print ma4.group()


ma5 = re.match(r'{..}', '{07}')   # . 匹配任意一个字符， ..匹配任意两个字符
print type(ma5)
print ma5.group()

ma6 = re.match(r'{[abc]}','{a}')
print ma6.group()

ma7 = re.match(r'{[a-z]}','{w}')
print ma7.group()

ma8 = re.match(r'{[a-zA-Z]}','{A}')
print ma8.group()

ma9 = re.match(r'{[a-zA-Z0-9]}','{9}')
print ma9.group()

ma10 = re.match(r'{[\w]}','{ }')
print ma10

ma11 = re.match(r'{[\W]}','{ }')
print ma11.group()


ma12 = re.match(r'\[[\w]\]', '[a]')
print ma12.group()