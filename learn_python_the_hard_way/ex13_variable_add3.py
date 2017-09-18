#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/15 22:47'


'''
笨办法学python P44
'''


from sys import argv

script, first, second, third = raw_input("Please input 4-alpha word: \n")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


# useage
# in terminal
# python ex13_variable.py 1st 2ed 3rd

'''
argv 和 raw_input() 有什么不同?
不同点在于用户输入的时机。
如果参数是在用户执行命令时就要输入，那就是 argv， 
如果是在脚本运行过程中需要用户输入，那就使用 raw_input()。
'''