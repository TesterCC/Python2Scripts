#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/62.html#mid=917
# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

from random import randint

# in video, use timeit, not convienient in code. so use import time instead.
import time


data = [randint(-10, 10) for _ in xrange(10)]
print "Random Int Data List >>>> ", data

print "--------------------------------"

# Method 1 -- 使用filter函数，过滤掉负数
start = time.clock()
r1 = filter(lambda x: x >= 0, data)
end = time.clock()
print "R1 run time: %f" % (end-start)
print(r1)


# Method 2 -- 使用列表解析，过滤掉负数 -- quicker -- 更快，故首选列表解析
start = time.clock()
r2 = [x1 for x1 in data if x1 >= 0]
end = time.clock()
print "R2 run time: %f" % (end-start)
print(r2)


# Method 1 and Method 2 is quicker than 2_1_0.py


# def count_runtime(*args):
#     start = time.clock()
#
#     end = time.clock()
#     print "Function run time: %f s." % (end - start)
# count_runtime(r2)