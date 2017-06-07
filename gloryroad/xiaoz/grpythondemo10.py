#coding:utf-8
'''
Created on 2016年2月17日

@author: PavilionLYX
'''
#GloryRoad Python Basic--lesson 6
import string

s = "hello python"
print s.capitalize()  #首字母大写

print "******************************"

print s.replace("python", "world")
print s.replace("hello", "hola")

s1 = "12341234123345674"

print s1.replace("4","go")
print s1.replace("4","go",2)#只替换前2个4

print string.replace(s1, '1','tt') #need import string

print "******************************"

ip = "192.168.0.1"
print ip.split('.')
print ip.split('.',1) #只分割第一个.


