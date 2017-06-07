#!/usr/bin/env python
# coding:utf-8

'''
选择排序
算法图解 P28
将数组元素按从小到 大的顺序排列。先编写一个用于找出数组中最小元素的函数。
'''


def findSmallest(arr):
    '''
    用于找出数组中最小元素的函数
    :param arr: arr
    :return: smallest_index
    '''
    smallest = arr[0]      # 存储最小的值
    smallest_index = 0     # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    '''
    对数组进行排序
    :param arr: arr
    :return: new Arr
    '''
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)     # 找出数组中最小的元素，并将其加入到新数组中
        newArr.append(arr.pop(smallest))     # pop(index) list.pop(obj=list[-1]) 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    return newArr

if __name__ == '__main__':
    print selectionSort([5,3,6,2,10])