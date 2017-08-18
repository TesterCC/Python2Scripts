#!/usr/bin/env python
# coding=utf-8

# Python大法之从HELL0 MOMO到编写POC(一)(二)
# https://bbs.ichunqiu.com/thread-26074-1-1.html


port = 1000

while 100<port<1024:
    print("[+]The PORT is : " + str(port))
    print("[-]The PORT is : %d" % port)   # 两种不同的写法
    port += 1     # port = port + 1