#-*- coding:utf-8 -*-#
'''
Created on 2015年11月10日
公开课第三讲 流程控制1  实现冒泡排序
求1到100的和
@author: PavilionLYX
'''

list=[45,13,24,3]
#冒泡排序实现
#13，45，24，3
#13，24，45，3
#13,24,3,45

#13,24,3,45
#13,3,24,45
#3,13,24,45

for i in range(1,len(list)):#range(0,len(list)-1)
    for j in range(0,len(list)-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        print list
        

