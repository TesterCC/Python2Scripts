#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/17 09:02'

"""
Python 2  中文和utf-8的编码转换
"""

a = u'王超'

# print()出来的结果和ipython中展示结果不同，特别注意

print(a)    # ipython u'\u738b\u8d85'

print("Encode to utf-8 {}".format(a.encode('utf-8')))   # utf-8   ipython '\xe7\x8e\x8b\xe8\xb6\x85'

print("Encode to unicode_escape {}".format(a.encode('unicode_escape')))   # unicode_escape ipython '\\u738b\\u8d85'

