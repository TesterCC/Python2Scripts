#!/usr/bin/env python
#coding=utf-8

# raw_input can't use in Python3
filename = raw_input('Enter file name:')
fobj = open(filename,'r')  #file in the same dir
for eachLine in fobj:
    print eachLine,
fobj.close()