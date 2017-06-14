#!/usr/bin/env python
# coding=utf-8

'''
调用栈举例
算法图解 P34
'''


def greet(name):
    print "hello, " + name + "!"
    greet2(name)
    print "getting ready to say bye ..."
    bye()


def greet2(name):
    print "how are you, " + name + "?"


def bye():
    print "ok bye!"


if __name__ == '__main__':
    greet("maggie")