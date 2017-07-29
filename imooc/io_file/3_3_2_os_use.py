#!/usr/bin/env python
#coding=utf-8


# 3-3 OS模块对文件和目录操作
# http://www.imooc.com/video/8045


import os


print(os.path.exists('./imooc.txt'))
print(os.path.exists('./imoocxxxx.txt'))
print(os.path.isdir('imooc.txt'))
print(os.path.isfile('imooc.txt'))
print(os.path.getsize('imooc.txt'))   # 返回大小，字节

print(os.path.basename('./imooc.txt'))   # 返回文件名
print(os.path.dirname('./imooc.txt'))   # 返回路径目录