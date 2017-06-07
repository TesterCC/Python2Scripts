# !/usr/bin/env python
# coding: utf-8

# http://www.imooc.com/video/8038

# f = open("wiki_crawler_info.txt")
# print type(f)
# print f.read()

f = open("1.txt")

print f.read()   # only write

f = open("1.txt", 'w')

f.write("test write")

f.close()

f1 = open("1.txt", 'a')

f1.write("\nprint 'a mode write test'.\n")
f1.close()

f2 = open('1.txt', 'r+')
f2.write("test r+")
f2.close()

