#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/25 05:51'

'''
Python基础 2-2.7 while循环应用
1. 计算1~100的累积和（包含1和100）
'''

i = 0
sum = 0

while i <= 100:
    sum = sum + i
    i += 1

print("1~100加法总和为: %d" % sum)