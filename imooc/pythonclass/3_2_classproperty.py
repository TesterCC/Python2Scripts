#!/usr/bin/python env
#coding=utf-8

'''
http://www.imooc.com/video/13263
 3-2 Python面向对象-定义类的属性
'''

class Programmer(object):

    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    print dir(programmer)
    print programmer.__dict__
    print programmer.get_weight()
    print programmer._Programmer__weight