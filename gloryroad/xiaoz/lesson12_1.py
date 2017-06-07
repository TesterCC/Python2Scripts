#coding:utf-8
'''
Created on 2016年2月25日

@author: PavilionLYX
'''
import re
# r=r'ab' #match rule, r means raw data，不需要转义
# print re.findall(r,'abcdefgabcdjjjab')
# print '\n'
# print '\\n'
# print r'\n'

f=open(r"D:\readme.txt")  #\r被转义
print f.read()
f.close()

r=r'1\*2'  #*为元字符，需要加转义符
print re.findall(r,'01*23450101*233')

r1=r'^123' # ^匹配行首
print re.findall(r1, '1234512345123')

r2=r'45$' # ^匹配行尾
print re.findall(r2, '123451234512345')

r3=r'3.5' # .匹配任意单字符
print re.findall(r3, '1234512345')

r4=r'a[a-zA-Z0-9]c'  #  []匹配指定的一个字符集
print re.findall(r4, 'abc,aCc,a5c,a3c,cfg,BBa,--a')

r5=r'a[^0-9]c'   #  [^ ]补集匹配不在区间范围内的字符
print re.findall(r5,'abc,aCc,a5c,a3c,cfg,BBa,--a')  

#16 min