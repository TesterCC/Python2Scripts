#!/usr/bin/python env
#coding=utf-8

'''
http://www.imooc.com/video/13268
4-2 Python面向对象-对象的实例化
'''


class Programmer(object):

    def __new__(cls, *args, **kwargs):
        print 'call __new__ method'
        print args
        return super(Programmer, cls).__new__(cls, *args, **kwargs)

    def __init__(self, name, age):
        print 'call __init__ method'
        self.name = name
        self.age = age

if __name__ == '__main__':
    programmer = Programmer('Albert', 25)
    print programmer.__dict__