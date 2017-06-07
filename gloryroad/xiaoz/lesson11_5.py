#coding:utf-8
'''
Created on 2016年2月22日

@author: PavilionLYX

实例：将程序抛出的异常截获存入log文件，抛给用户
一个友好的提示。

'''
#lesson 11
from robot.utils.argumentparser import ArgFileParser

#Exception 1
try:
    raise Exception("test raise")
    1/0
except Exception,e:
    f=open("error.log","w")
    f.write(str(e)+"\n")
    f.close()
    print e

class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.arg = arg

#Exception 2
try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e