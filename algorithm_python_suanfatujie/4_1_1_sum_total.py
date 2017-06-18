#!/usr/bin/env python
# coding=utf-8

'''
快速排序
算法图解 P45
将列表中数字相加并返回结果。
'''


L = [1, 2, 3, 4]


def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

if __name__ == '__main__':
    print sum(L)