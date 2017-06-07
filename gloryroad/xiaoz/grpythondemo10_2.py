#coding:utf-8
'''
Created on 2016年2月18日

@author: PavilionLYX
'''

#lesson 6

def f(x):
    if x%2 == 0:
        return True

print filter(f,range(10))

#匿名函数实现取出1到100之间的偶数

print filter(lambda x:x%2==0, range(1,101))

print "**********************************"

name = ["aa","bb","cc"]
age= [15,17,20]
city=["Beijing","Shanghai","Guangzhou"]
print zip(name,age,city)
print map(None,name,age,city)

print "**********************************"

gender=["male","female"]
print zip(name,gender,age,city)
print "-----------------------------------"
print map(None,name,gender,age,city)

print "**********************************"

a=[1,2,3]
b=[4,5,6]

def add(x,y):
    return x+y

print map(None,a,b)
print map(add,a,b) #第一个参数也可以是一个自定义的函数

print "**********************************"
print reduce(add,range(1,101))




