#!/usr/bin/env python
# coding=utf-8

# Python 全栈案例初体验  2-5 Python_技巧介绍
# http://www.imooc.com/video/15371
# 列表字典推导式


import string

print(string.letters)    # 产生大小写的全部字母, python3 ascii_letters
print(string.punctuation)    # 产生特殊字符
print(string.letters[0])

print("----------------------")

a_list = range(10)
print(a_list)     # list type
# print(type(a_list))

b_list = [i*i for i in a_list]
print(b_list)     # list type

b_dict = {i: string.letters[i] for i in a_list}
print(b_dict)
print("=========================================")

# 列表字典解析式
for i in b_list:
    print i,
print

for i in range(len(b_list)):
    print a_list[i],
print

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据下标和数据，一般用在 for 循环当中。
for index, value in enumerate(b_list):
    print index, '->', value,

print
print("=========================================")

# 打印字典的解析式
for i in b_dict:
    print i, '->', b_dict[i],
print

for key, value in b_dict.iteritems():   # 在python 3.x 中就是 items()
    print key, '->', value,

