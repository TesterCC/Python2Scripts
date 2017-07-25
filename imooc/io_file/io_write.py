#!/usr/bin/env python
#coding=utf-8


f = open("hello.txt")

print type(f)
# print dir(f)
print f.read()

g = open("1.txt", 'w')
# only write, if file is not exist, will create file
# only write, if file is exist, will clear file content and open.
g.write("test write")
g.close()


h = open("hello.txt", 'a')   # add at end , not clear
h.write("print 'write test'!\n")
h.close()


i = open("hello.txt", 'r+')   # insert begin and replace begin
i.write("test r+\n")
i.close()

j = open("hello.txt", 'w+')    # clear content and write str
j.write("test w+\n")
j.close()

# practice
k = open("imooc.txt", 'a')
k.write("www.imooc.com\n")
k.close()

