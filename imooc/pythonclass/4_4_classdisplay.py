#!/usr/bin/python env
#coding=utf-8

'''
http://www.imooc.com/video/13270
4-4 Python面向对象-类的展现
'''


class Programmer(object):

    def __init__(self, name, age):
        self.name = name

        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('Age must be int type.')

    def __str__(self):
        return '%s is %s years old.' % (self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()


if __name__ == '__main__':
    p = Programmer('Albert', 25)
    print p
    print dir(p)