#!/usr/bin/env python
# coding=utf-8
# P15序列化操作


try:
    import cPickle as pickle
except ImportError:
    import pickle
# cPickle效率更高

d = dict(url='index.html', title='首页', content='内容')
r = pickle.dumps(d)   # 将任意对象序列化成一个str
print(r)

f = open(r'D:\testercc_github_code\Python2Scripts\the_fighting_of_python_spider\dump.txt', 'wb')
r2 = pickle.dump(d,f)
print(r2)
f.close()
