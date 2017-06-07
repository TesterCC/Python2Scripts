#!/usr/bin/env python
#coding=utf-8

#Testing Python -- P21


class Calculate(object):
    def add(self,x,y):
        return x+y

if __name__ == '__main__':
    calc = Calculate()
    result = calc.add("Hello","World")
    print result