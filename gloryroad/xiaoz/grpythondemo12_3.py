#coding:utf-8
'''
Created on 2016年2月19日

@author: PavilionLYX
'''

#lesson 8 Class
class MyCounter(object):
    __secretCount = 0
    publicCount = 0
    
    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print self.__secretCount

n=MyCounter()
n.count()

print n.publicCount
# print n.__secretCount  #python不允许实例化的类访问私有数据

print n._MyCounter__secretCount  #_MyCounter__

        


