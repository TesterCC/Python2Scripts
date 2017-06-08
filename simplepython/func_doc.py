#!/usr/bin/env python
#coding:utf-8

# 简明python教程 Python2版  A byte of python -- Python2

def printMax(x,y):
    '''
    Print the maximum of 2 numbers.
    
    The two values must be integers.
    '''
    x = int(x)  # convert to integers, if possible
    y = int(y)

    if x>y:
        print x,'is maximum.'
    else:
        print y,'is maximum.'


printMax(3,5)
print printMax.__doc__
