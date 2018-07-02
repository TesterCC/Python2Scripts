#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/2 09:05'

"""
Effective Python编写高质量Python代码的59个有效方法  P6
Python2  str(包含原始8位，等价Python3的bytes)
Python2  unicode(包含Unicode字符)

Python2
str.decode('utf-8')      -> unicode
unicode.encode('utf-8')  -> str

Python编程：编解码放在界面最外围来做，程序核心部分应该使用Unicode字符类型，且不要对字符编码做任何假设。
"""


def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str

    return value


def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str

    return value


if __name__ == '__main__':
    print('str to unicode:')
    text1 = '编程'
    print(type(text1))
    text1u = to_unicode(text1)
    print(type(text1u))
    print(text1u)     # unicode

    print('unicode to str:')
    text2 = u'\u7f51\u7edc\u6280\u672f'    # unicode python2, python3会直接打印出转化后的汉字文本
    print(type(text2))
    text2u = to_str(text2)
    print(type(text2u))
    print(text2u)     # str

