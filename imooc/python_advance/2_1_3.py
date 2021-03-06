#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/62.html#mid=917
# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

from random import randint


# Method3 -- 筛出字典{'Lilei':79, 'Lucy':92 ...}中值高于90的项
# 随机生成一个字典
d = {x: randint(60, 100) for x in xrange(1, 21)}
print(d)

r = {k: v for k, v in d.iteritems() if v > 90}
print(r)






