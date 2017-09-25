#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/25 05:51'

'''
Python基础 2-2.7 while循环应用
2.计算1~100之间偶数的累积和（包含1和100）
'''

i = 1
sum = 0

while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i += 1

print("1~100之间偶数的累积和: %d" % sum)