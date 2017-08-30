#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/8/30 14:44'



'''
python网络爬虫实战--胡松涛
P25
'''


s = "dbca234"
s0 = "xxxxxxxx"
s1 = "5555"
s2 = "DDDggg334BBA"
s3 = "   "
s4 = "GGGG"
s5 = "0123456789abcdef"


# 大小写转换类
print(s2.lower())   # 字母大写转换成小写
print(s.upper())    # 字母小写转换成大写
print(s2.swapcase())    # 字母大写转换成小写同时字母小写转换成大写
print(s.title())   # 首字母大写
print(s.capitalize())  # 首字母大写

print("--------------------------")

# 字符串搜索和替换
print(s5.find("f"))
print(s5.find("b"))

print("--------------------------")

# 字符串分割和组合

print("--------------------------")

# 字符串测试
print(s0.isalpha())    # str是否全是字母，至少有一个字符
print(s1.isdigit())   # str是否全是数字，至少有一个字符
print(s3.isspace())   # str是否全是空白字符，至少有一个字符
print(s0.islower())    # str中的字母是否全是小写
print(s4.isupper())    # str中的字母是否全是大写
print(s.istitle())     # str是否时首字母大写