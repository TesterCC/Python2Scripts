#!/usr/bin/env python
# coding:utf-8

'''
二分法
函数binary_search接受一个有序数组和一个元素。如果指定的元素包含在数组中,这个函数将返回其位置。
算法图解 P7 
'''


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <=high:
        mid = (low + high)/2
        guess = list[mid]
        # print "guess value:",guess
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    my_list = [1,3,5,7,9,11]

    print binary_search(my_list,3)   # my_list,find element value  index 1
    print binary_search(my_list,-1)  # None
    print binary_search(my_list,9)   # index 4
    print binary_search(my_list,8)   # None
    print binary_search(my_list,7)   # index 3