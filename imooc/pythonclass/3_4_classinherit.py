#!/usr/bin/python env
#coding=utf-8

'''
http://www.imooc.com/video/13265
3-4 Python面向对象-类的继承
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


class BackendProgrammer(Programmer):
    def __init__(self, name, age, weight, language):
        super(BackendProgrammer, self).__init__(name, age, weight)
        self.language = language


if __name__ == '__main__':
    programmer = BackendProgrammer('Albert', 25, 80, 'Python')
    print dir(programmer)
    print programmer.__dict__
    print type(programmer)
    print isinstance(programmer, Programmer)