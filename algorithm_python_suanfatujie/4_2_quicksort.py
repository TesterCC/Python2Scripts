#!/usr/bin/env python
# coding=utf-8

'''
快速排序
算法图解 P52
快速比较多个数字大小 递归
'''

import random


def quicksort(array):
    if len(array) < 2:
        return array     # 基线条件:为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]   # 递归条件
        less = [i for i in array[1:] if i <= pivot]  # 由所有小于或等于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]   # 由所有大于基准值的元素组成的子数组

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    L = [10, 5, 2, 3, 5]
    R = [random.randint(1, 20) for i in range(7)]  # 返回1到20之间随机整数7歌
    print(quicksort(L))
    print("-------------------")
    print(quicksort(R))