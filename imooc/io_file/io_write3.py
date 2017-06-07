#!/usr/bin/env python
#coding=utf-8


f = open('imooc3.txt', 'w')

for i in range(10000):
    f.write('test write ' + str(i) + '\n')

f.close()