# coding:utf-8
# !/usr/bin/env python

# Testing Python pdf P18 P20


class Calculate(object):

    def add(self, x, y):
        return x + y

if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2, 2)
    # result = calc.add("Hello", "World")
    print result


