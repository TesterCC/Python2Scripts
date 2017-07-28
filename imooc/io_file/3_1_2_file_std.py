#!/usr/bin/env python
#coding=utf-8

# 3.文件属性及OS模块使用
# http://www.imooc.com/video/8043


import sys

print(type(sys.stdin))

print("sys.stdin : ")
print(sys.stdin.mode)
# print(sys.version)
# print(sys.version_info)
print(sys.stdin.fileno())

print("sys.stdout : ")
print(sys.stdout.mode)
print(sys.stdout.fileno())

print("sys.error : ")
print(sys.stderr.mode)
print(sys.stderr.fileno())
