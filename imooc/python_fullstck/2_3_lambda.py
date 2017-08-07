#!/usr/bin/env python
# coding=utf-8

# Python 全栈案例初体验  2-3
# http://www.imooc.com/video/15369


func = lambda x: x**2   # 冒号前面是传入参数，后面是一个处理传入参数的单行表达式。

print(func(3))


a_list = range(10)

# c = map(func, a_list)

c = map(lambda x: x**2, a_list)   # 匿名函数执行完后就不存在了，一般直接写

print(c)