#!/usr/bin/python env
#coding=utf-8

'''
http://www.imooc.com/video/13269
4-3 Python面向对象-类与运算符
'''


class Programmer(object):

    def __init__(self, name, age):
        self.name = name

        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('Age must be int type.')

    def __eq__(self, other):
        if isinstance(other, Programmer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programmer.')

    def __add__(self, other):
        if isinstance(other, Programmer):
            return self.age + other.age
        else:
            raise Exception('The type of object must bs Programmer.')

if __name__ == '__main__':
    p1 = Programmer('Albert', 25)
    p2 = Programmer('Bill', 30)
    print p1 == p2
    print p1 + p2