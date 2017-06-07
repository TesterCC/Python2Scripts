#-*- coding:utf-8 -*-#
'''
Created on 2015年11月10日
公开课第三讲 流程控制1  判断闰年
@author: PavilionLYX
'''
year = int(raw_input("Please input the year(e.g. 2008):"))

if (year%100==0 and year%400 ==0) or (year%100 != 0 and year%4==0):
    print "%d is leap year" %year
else:
    print "%d is not leap year" %year