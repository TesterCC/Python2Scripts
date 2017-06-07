#coding:utf-8
'''
Created on 2016年2月19日

@author: PavilionLYX
'''
import copy

def changeme(mylist):
    mylist[0]=18
    print "in:",mylist
    
mylist=[1,2,3,4,5]
copylist=copy.deepcopy(mylist)
changeme(mylist)
print "out:mylist",mylist
print "out:copylist",copylist
