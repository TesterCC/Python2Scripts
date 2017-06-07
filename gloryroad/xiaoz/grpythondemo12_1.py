#coding:utf-8
'''
Created on 2016年2月19日

@author: PavilionLYX
'''
from twisted.conch.test.test_agent import agent

#lesson 8 Class

class User(object):
    "User information"
#     name='zz'
#     age=18

    count=0
    
    def __init__(self, name, age):  #类的构造函数，初始化方法
        self.name = name
        self.age = age
        User.count+=1
    

    def who(self):
        print "My name is "+ self.name + ",I'm " + str(self.age)+" years old."
        
    def __del__(self):
        class_name=self.__class__.__name__
        print class_name,"destroyed"
        
#实例化对象
u1 = User('zz',18)
u1.who()
print u1.count

u2 = User('aa',20)
u2.who()
print u2.count

print "========================="
print User.__doc__  #类的文档字符串
print User.__name__ #Class Name
print User.__module__  #类定义所在的模块
print User.__bases__  #类的所有父类构成元素
print User.__dict__  #类的属性

del u1

