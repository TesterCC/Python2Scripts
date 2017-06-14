#!/usr/bin/env python
# coding=utf-8

'''
递归调用栈举例  阶乘 5! = 5*4*3*2*1
算法图解 P36
'''


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


if __name__ == '__main__':
    print(fact(3))