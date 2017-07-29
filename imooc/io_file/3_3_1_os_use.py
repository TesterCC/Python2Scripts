#!/usr/bin/env python
#coding=utf-8


# 3-3 OS模块对文件和目录操作
# http://www.imooc.com/video/8045


import os


# 偏底层,文件的创建->写入->读取->关闭
fd = os.open('imooc00.txt', os.O_CREAT | os.O_RDWR)

n = os.write(fd, 'imooc')

l = os.lseek(fd, 0, os.SEEK_SET)

print(l)

str1 = os.read(fd, 5)

print(str1)

os.close(fd)

print(os.access('imooc00.txt', os.F_OK))
print(os.access('imooc00.txt', os.R_OK))
print(os.access('imooc00.txt', os.W_OK))
print(os.access('imooc00.txt', os.X_OK))
print(os.access('imooc001.txt', os.F_OK))

print(type(os.listdir('./')))
print(os.listdir('./'))
os.rename('imooc00.txt', 'imooc001.txt')
os.remove('imooc001.txt')


# create directory
os.mkdir('test1')
os.makedirs('test/test1/test2')
os.rmdir('test1')
os.removedirs('test/test1/test2')


