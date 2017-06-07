#!/usr/bin/python env
#coding=utf-8

'''
http://www.imooc.com/video/13300
3-5 类的多态
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

    def self_introduction(self):
        print 'My name is %s \nMy favorite language is %s.\n' % (self.name, self.language)


def introduce(programmer):
    if isinstance(programmer, Programmer):
        programmer.self_introduction()
    # programmer.self_introduction()       # 多态是可以自动优先重载,所以只有这句，不加判断也可以



if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    backend_programmer = BackendProgrammer('Tim', 30, 70, 'Python')
    # print isinstance(programmer, Programmer)
    # print isinstance(backend_programmer, Programmer)
    # print "---------------------------"
    introduce(programmer)
    introduce(backend_programmer)