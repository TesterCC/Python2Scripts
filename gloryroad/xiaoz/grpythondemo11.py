#coding:utf-8
'''
Created on 2016年2月19日

@author: PavilionLYX
'''

#lesson 7
import copy

a=[0,1,2,3,[4,5,6]]

print id(a)
print id(a[0])
print id(a[4][0])
print "+++++++++++++++++++++"

b=a
print id(b)
print id(b[0])
print id(b[4][0])
print "+++++++++++++++++++++"

c=copy.copy(a)  #import copy,浅拷贝
print c
print id(c)
print id(c[0])
print id(c[4][0])
print "+++++++++++++++++++++"

c[0]=9
print c
print a
print "+++++++++++++++++++++"

c[4][0]=44
print c
print a

#浅拷贝是对引用的copy，只copy复制项，对象内部的资源依然是引用

print "=============================="


d=copy.deepcopy(a)
print d
print id(d)
print id(d[0])
print id(d[4][0])
print "=============================="

d[0]=9

print d
print a

d[4][0]=444
print d
print a