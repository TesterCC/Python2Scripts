# coding:utf-8

'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681963899940a998c0ace64bb5ad45d1b56b103c48000
列表生成式

'''

import os


print [d for d in os.listdir('.')]   # os.listdir可以列出文件和目录
print "-----------------------------"

d = {'x': 'A', 'y': 'B', 'z': 'C' }
S=[]
for k, v in d.iteritems():
    print k, '=' , v
    S.append(k+'='+v)
print S

print "-----------------------------"

print [k+'='+v for k,v in d.iteritems()]
print "-----------------------------"



T = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in T]     # 把一个list中所有的字符串变成小写
print [s.upper() for s in T]     # 把一个list中所有的字符串变成大写


print "-----------------------------"
LL = ['Hello','world',2016,0116]

newLL = [isinstance(s,str) and s.lower() or s for s in LL ]

print newLL

['hello', 'world', 2016, 78]