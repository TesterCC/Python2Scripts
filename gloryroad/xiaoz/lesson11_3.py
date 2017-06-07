#coding:utf-8
'''
Created on 2016年2月22日

@author: PavilionLYX

实例：try-finally和try-except嵌套使用，保证
无论是否发生异常写完之后及时将文件关闭
'''
#lesson 11

try:
    f=open("test.txt","r")#"w"
    try:
        f.write("This is my test file for exception handing.")
    finally:
        print "Going to close the file."
        f.close()
        print "Closed the file."
except IOError: 
    print "Error:can't find file or read data."

