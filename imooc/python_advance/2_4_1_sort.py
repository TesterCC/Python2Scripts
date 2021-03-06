#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/27 23:45'

'''
2-4 如何根据字典中值的大小, 对字典中的项排序
http://coding.imooc.com/lesson/62.html#mid=824
成绩以字典形式存储，如：{'Tom': 99, 'Lily': 88, 'Lucy': 70}
根据成绩高低，计算成绩排名

解决方案：
使用内置函数sorted
1.利用zip将字典数据转化为元组   利用元组index 0来排序
'''

from random import randint


# create score dict
d = {x: randint(60, 100) for x in "xyzabc"}
print(d)

print("------------------------")
print(sorted(d))

print(d.keys())    # keys
print(d.values())   # values

print('------------zip-----------')
print(zip(d.values(), d.keys()))      # score in index 0
print(zip(d.itervalues(), d.iterkeys()))      # save more space

print('------------sorted zip-----------')
print(sorted(zip(d.itervalues(), d.iterkeys())))