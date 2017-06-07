#!/usr/bin/python env
#coding=utf-8

'''
http://www.imooc.com/video/13271
4-5 Python面向对象-类的属性控制
'''

class Programmer(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, name):
        # return getattr(self, name)   # -- wrong 会造成递归调用，超出递归限制
        # return self.__dict__[name]   # -- wrong 会造成递归调用，超出递归限制
        return super(Programmer, self).__getattribute__(name)  # right

    def __setattr__(self, name, value):
        # setattr(self, name, value)  # -- wrong 会造成递归调用，超出递归限制
        self.__dict__[name] = value   # right

if __name__ == '__main__':
    p = Programmer('Albert', 25)
    print p.name
    print p.age