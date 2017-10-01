#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/10/1 09:35'

'''
（面试题）给定一个字符串testStr，返回使用空格或者'\t'分割后的倒数第二个子串
testStr = "haha nihao a \t heihei \t woshi ni\n\tde \t hao \npengyou"
'''


testStr = "haha nihao a \t heihei \t woshi ni\n\tde \t hao \npengyou"

result = testStr.split()     # 默认设置处理空字符 space \n \t

print(result)
print(result[-2:-1])    # 分割后的倒数第二个子串

print("------join str-----")
print(" ".join(result))
