#!/usr/bin/env python
# coding:utf-8

'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001418612030427b1f1cf4ea04c41368e8a6753dca43070000
'''

# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n%2 == 1    # return jishu


print filter(is_odd,[1,2,3,4,5,6,7])

print "--------------------------------"
print filter(is_odd, range(3,16))
print "--------------------------------"



# 把一个序列中的空字符串删掉

def not_empty(s):
    return s and s.strip()


print filter(not_empty, ['A','','B', None, 'C', '   '])