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
s2 = "DDgDg334gBBA"
s3 = "   "
s4 = "GGGG"
s5 = "0123456789abcdef"
s6 = "a__dasd__dasA__sdfa"
s7 = u"测试"


# 大小写转换类
print(s2.lower())   # 字母大写转换成小写
print(s.upper())    # 字母小写转换成大写
print(s2.swapcase())    # 字母大写转换成小写同时字母小写转换成大写
print(s.title())   # 首字母大写
print(s.capitalize())  # 首字母大写

print("--------------------------")

# 字符串搜索和替换
print(s5.find("f"))
print(s5.find("b", 4))
print(s4.count('G'))    # 计算在G在s4中出现的次数
print(s4.count('G', 2))    # 计算在G在s4中出现的次数
print(s4.replace('G', 'A'))     # 把G替换为A
print(s4.replace('G', 'A', 2))
print(s6.strip("a"))   # 移除字符串头尾指定字符
print(s6.lstrip("a"))   # 截掉字符串左边的空格或指定字符
print(s6.rstrip("a"))   # 截掉字符串右边的空格或指定字符

print("--------------------------")

# 字符串分割和组合
print(s2.split("g", 2))
print(s6.split("__"))

L = ["test", "dsd", "77"]
print(s0.join(L))   # 把L代表的序列用s0字符串链接起来

print("--------------------------")

# 字符串编码解码
print(s1.decode("utf-8"))    # 将以utf-8编码的s1解码成unicode编码
print(s7.encode("utf-8"))    # 将以unicode编码的s7编码成utf-8, 也可以是gb2312,gbk,big5
print(s7.encode("gbk"))    # 将以unicode编码的s7编码成utf-8, 也可以是gb2312,gbk,big5

print("--------------------------")

# 字符串测试
print(s0.isalpha())    # str是否全是字母，至少有一个字符
print(s1.isdigit())   # str是否全是数字，至少有一个字符
print(s3.isspace())   # str是否全是空白字符，至少有一个字符
print(s0.islower())    # str中的字母是否全是小写
print(s4.isupper())    # str中的字母是否全是大写
print(s.istitle())     # str是否时首字母大写