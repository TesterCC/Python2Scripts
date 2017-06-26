#!/usr/bin/env python
# coding=utf-8

'''
4-3-1 比较合并排序和快速排序
算法图解 P53
'''
from time import sleep
import random


# runtime is O(n), but print_items() is faster than print_items2()
def print_items(list):
    for item in list:
        print item


def print_items2(list):
    for item in list:
        sleep(1)
        print item

if __name__ == '__main__':
    L = [10, 5, 2, 3, 5]
    R = [random.randint(1, 20) for i in range(7)]  # 返回1到20之间随机整数7歌
    print_items(L)
    print_items2(L)
    # print("-----------------------------")
    # print_items(R)
    # print_items2(R)
