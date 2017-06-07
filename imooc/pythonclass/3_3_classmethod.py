#!/usr/bin/python env
#coding=utf-8

'''
http://www.imooc.com/video/13264
3-3 Python面向对象-定义类的方法
'''

class Programmer(object):

    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight


    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight


    def self_introduction(self):
        print 'My name is %s \nI am %s years old\n' % (self.name, self._age)


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    print dir(programmer)
    print Programmer.get_hobby()
    print programmer.get_weight
    programmer.self_introduction()