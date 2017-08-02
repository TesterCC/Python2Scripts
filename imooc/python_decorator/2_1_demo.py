#!/usr/bin/env python
#coding=utf-8


'''
http://www.imooc.com/video/10832
2-1 python装饰器之闭包1
'''


passline = 60   # total score 100


def func(val):
    passline = 90   # total score 150, priority
    print('%x' % id(val))    # %x以十进制打印
    if val >= passline:
        print ('pass')
    else:
        print ('failed')

    def in_func():   # will add val in function's attribute -- tuple
        print(val)
    in_func()
    return in_func

f = func(89)
f()  # is in_func
print(f.__closure__)
