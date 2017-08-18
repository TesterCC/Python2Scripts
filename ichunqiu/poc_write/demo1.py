#!/usr/bin/env python
# coding=utf-8

# Python大法之从HELL0 MOMO到编写POC(一)(二)
# https://bbs.ichunqiu.com/thread-26074-1-1.html


demo = open('MOMO.txt', "wb")

# 写入txt
demo.write("MOMO is Tester!\ntest")
demo.close()


print(u"是否关闭：", demo.closed)
print(u"访问模式：", demo.mode)
print(u"文件名称：", demo.name)
print(u"末尾是否加空格：", demo.softspace)


# 读取txt
demo1 = open('MOMO.txt', 'r')
re = demo1.readlines()
print(re)