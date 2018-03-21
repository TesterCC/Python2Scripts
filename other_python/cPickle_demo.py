#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/3/21 15:03'


"""
python中cPickle用法例子分享
http://www.jb51.net/article/45165.htm

在python中，一般可以使用pickle类来进行python对象的序列化，
而cPickle提供了一个更快速简单的接口，如python文档所说的：“cPickle -- A faster pickle”。
"""

import cPickle

data = range(1000)

# dump： 将python对象序列化保存到本地的文件
cPickle.dump(data, open("data.txt", "wb"))
print(type(data))

# load：载入本地文件，恢复python对象
data = cPickle.load(open("data.txt", "rb"))
print(type(data))

# dumps：将python对象序列化保存到一个字符串变量中。
data_string = cPickle.dumps(data)
print(type(data_string))

# loads：从字符串变量中载入python对象
data = cPickle.loads(data_string)
print(type(data))


