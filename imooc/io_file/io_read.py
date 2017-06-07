#!/usr/bin/env python
#coding=utf-8


f = open("imooc.txt")
print f.readline()
print f.readline(5)
print f.readline()
f.close()
print("---------------------------")

g = open("imooc.txt")
list_c = g.readlines(1)
g.close()
print list_c
print("---------------------------")

h = open("imooc.txt")
iter_h = iter(h)
lines = 0

for line in iter_h:
    lines += 1
print lines   # print line count
