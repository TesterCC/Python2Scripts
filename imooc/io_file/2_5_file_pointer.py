#!/usr/bin/env python
#coding=utf-8


# 2-5 python文件操作之文件指针
# http://www.imooc.com/video/8042
# 在python27中，用0表示初始，1表示当前位置，2表示末尾位置


import os


f = open('imooc4.txt', 'r+')

print(f.tell())     # current file position, an integer (may be a long integer).
print(f.read(3))
print(f.tell())
print("-------------------")

# 让current回到0
f.seek(0, os.SEEK_SET)
print(f.tell())

# set to end
f.seek(0, os.SEEK_END)
print(f.tell())
print(f.read())
print("-------------------")

# 向后返回5个字节
f.seek(-5, os.SEEK_CUR)
print(f.tell())
print(f.read())
print(f.tell())