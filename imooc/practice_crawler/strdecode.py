#!/urs/bin/env python
# coding=utf-8

import sys


print("Default encoding is : "+sys.getdefaultencoding())
print("-----------------------------------")

s = "abc"
su = u"abc"

print(s.encode("utf8"))
print(su.encode("utf-8"))
print("-----------------------------------")

s2 = "我用Python"
su2 = u"我用Python"   # 已经是unicode

# print(s2.encode("utf8"))   # 调encode之前必须确保前面的变量是unicode
print(s2.decode("utf8").encode("utf8"))    # windows gb2312, linux/unix ascii
# decode默认调用系统编码做解码，直接encode("utf8")会报错

print(su2.encode("utf-8"))     # su2 已经是unicode