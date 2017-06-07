#!/usr/bin/env python
#coding=utf-8


f = open('imooc1.txt', 'w')

f.write('test write')
f.writelines('123456')
f.writelines(['A1','B2','C3'])
f.writelines(('A','B','C'))

f.flush()
f.close()
