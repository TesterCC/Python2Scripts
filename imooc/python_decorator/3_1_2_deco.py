#!/usr/bin/env python
#coding=utf-8


'''
http://www.imooc.com/video/10835
3-1 python装饰器
'''


def deco(func):
    def in_deco(x, y):
        print('in deco')
        func(x, y)
    print('call deco')
# 不写return的话默认返回 None
    return in_deco


# 装饰器调用过程
@deco      # 1. call deco(bar) -> return in_deco   # 2.bar = in_deco  3.bar() same to call in_deco() -> bar()
def bar(x, y):
    print("in bar", x+y)

print(type(bar))

bar(1, 2)
