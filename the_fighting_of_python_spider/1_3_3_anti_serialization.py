#!/usr/bin/env python
# coding=utf-8
# P16序列化操作


try:
    import cPickle as pickle
except ImportError:
    import pickle
# cPickle效率更高

f = open('dump.txt', 'rb')
d = pickle.load(f)    # 将文件直接反序列化为对象
print(d)
print(type(d))

