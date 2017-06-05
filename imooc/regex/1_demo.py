#!/usr/bin/python
# coding:utf-8

import re

str1 = 'imooc python'

print str1.find('11')
print str1.find('python')  # match start to index 6
print str1.startswith('imooc')
print str1.endswith('python')


print "============================"
pa2 = re.compile(r'imooc\n')
ma2 = pa2.match(str1)
print ma2


print "============================"
pa = re.compile(r'imooc')
print type(pa)

ma = pa.match(str1)
print ma.group()
print ma.span()
print ma.string

print "================22============"
pa1 = re.compile(r'imooc',re.I)

ma1 = pa1.match('ImOoc python')

print ma.group()
print ma.string

print "================333============"
pa3 = re.compile(r'(imooc)',re.I)

ma3 = pa3.match(str1)

print ma3.groups()


print "==============4444============"
ma0 = re.match(r'imooc',str1)

print ma0.group()


