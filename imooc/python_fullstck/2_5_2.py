#!/usr/bin/env python
# coding=utf-8

# Python 全栈案例初体验  2-5 Python_技巧介绍
# http://www.imooc.com/video/15371
# 函数为第一公民的应用


import string

a_list = [1, 3, 8, 'a', 'b', "^-^", 10]


def a_function(x):
    if isinstance(x, int):
        if 0 <= x < len(string.letters):
            return string.letters[x]
    else:
        return 'x not valid.'


def b_function(a_list=None, func=None):   # 把函数作为参数传递到另一个函数中
    for index, value in enumerate(a_list):
        print(index, '->', func(value))
    return None

if __name__ == '__main__':
    b_function(a_list, func=a_function)

