#coding:utf-8
'''
Created on 2016年2月22日

@author: PavilionLYX

'''
#lesson 11

try:
    f=open("test.txt","r") #"w"
    f.write("This is my test file for exception handing.")
except IOError,e:
    print e 
    print "Error:can't find file or read data."
else:
    print "Written content in the file successfully."

f.close()
print "Done."

