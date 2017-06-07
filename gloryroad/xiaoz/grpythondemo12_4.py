#coding:utf-8
'''
Created on 2016年2月19日

@author: PavilionLYX
'''

#lesson 8 Class
class Test1(object):
    def test1(self):  #实例方法
        print "object"
        
    @classmethod  #表示这个是类方法
    def test2(cls):
        print "class"
    
    @staticmethod  #静态方法
    def test3():
        print "static"

class Test2(Test1):
    @classmethod
    def test2(cls):
        print cls
        print "test2 object"
    
      
#实例调用        
f1=Test1()
f1.test1()

Test1.test1(f1)

print "-------------------------------------"

#类方法调用
f1.test2()
Test1.test2()  #类方法不需要传递实例的引用
print "-------------------------------------"

#静态方法
f1.test3()
Test1.test3()    
print "-------------------------------------"
        
Test2.test2()

