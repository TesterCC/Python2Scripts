#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-20 11:48'

"""
高效开发 红书 P235   开发者使用yield定义自己的的迭代器

调用流程：
调用迭代器的next()函数-->执行迭代器函数-->返回yield的结果作为迭代返回元素

在Python中，使用yield关键字定义的迭代器也被称为生成器
"""

# 定义一个迭代器函数
def demoIterator():
    print("I'm in the 1st call of next()")
    yield 1
    print("I'm in the 2ed call of next()")
    yield 3
    print("I'm in the 3rd call of next()")
    yield 9

for i in demoIterator():
    print(i)

print(type(demoIterator()))   # <type 'generator'>

