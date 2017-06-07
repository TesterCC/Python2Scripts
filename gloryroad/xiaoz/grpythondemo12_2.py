#coding:utf-8
'''
Created on 2016年2月19日

@author: PavilionLYX
'''

#lesson 8 Class

class User(object):
    "User information"
#     name='zz'
#     age=18

    
    def __init__(self, name, age):  #类的构造函数，初始化方法
        self.name = name
        self.age = age
    

    def who(self):
        print "My name is "+ self.name + ",I'm " + str(self.age)+" years old."
        
    def __del__(self):
        class_name=self.__class__.__name__
        print class_name,"destroyed"

class Student(User):
    def __init__(self,name,age,height):
        User.__init__(self,name,age)
        self.height=height  #调用新的成员变量
        
    def who(self):
        User.who(self)
        print "My height is "+str(self.height)+"."
        
Student('cc',18,177).who()
    
        


