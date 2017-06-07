#!/usr/bin/env python
#coding=utf-8


'''
http://www.imooc.com/video/10832
2-1 python装饰器之闭包1
'''


passline = 60


def func(val):
    passline = 90
    if val >= passline:
        print ('pass')
    else:
        print ('failed')

    def in_func():
        print(val)
    in_func()


if __name__ == '__main__':
    func(89)
