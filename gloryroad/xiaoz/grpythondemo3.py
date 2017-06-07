#-*- coding:utf-8 -*-#
'''
Created on 2015年11月10日
公开课第三讲 流程控制1
@author: PavilionLYX
'''
x=int(raw_input("Please input score x:"))
y=int(raw_input("Please input score y:"))

if x>60 and y>60 :
    print "pass all"
elif x>60 or y>60:
    print "pass one"
else:
    print "fail all"