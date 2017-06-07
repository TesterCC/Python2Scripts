#!/usr/bin/env python
#coding=utf-8

'''
Testing Python.pdf - P21
'''


class Calculate(object):

    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x),type(y)))



if __name__ == '__main__':
    calc = Calculate()
    # result = calc.add(2, 2)
    result = calc.add("Hello", "World")
    print result




