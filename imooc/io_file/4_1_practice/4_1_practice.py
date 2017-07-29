#!/usr/bin/env python
#coding=utf-8

# 4-1 文件练习
# http://www.imooc.com/video/8046

'''
任务：
使用Python管理ini文件：实现查询，添加，删除，保存

目的：
1.掌握文件基本操作
2.认识ini文件
3.了解ConfigParse
'''


import ConfigParser

cfg = ConfigParser.ConfigParser()

# cfg.read('imooc.ini')     # .txt也可以
cfg.read('imooc.txt')     # .ini也可以

print(cfg.sections())     # return [session]
print(cfg.items('userinfo'))     # return item
print(cfg.items('study'))     # return item

print("----------------------")
# print seesion and item
for se in cfg.sections():
    print se
    print cfg.items(se)

print("----------------------")

# change data
cfg.set('userinfo', 'pwd', '12345')
print(cfg.items('userinfo'))

# insert data
cfg.set('userinfo', 'email', 'test@test.com') # but didn't write in imooc.ini
print(cfg.items('userinfo'))

# delete data
cfg.remove_option('userinfo', 'email')
print(cfg.items('userinfo'))






