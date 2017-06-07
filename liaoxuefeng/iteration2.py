# coding:utf-8

'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868196435255fcca20a1630446ea2dd434a7176e152000
'''

from collections import Iterable

print isinstance('abc', Iterable)   # str
print isinstance([1,2,3], Iterable)   # list
print isinstance(123, Iterable)   # int

print "-----------------"

for i,val in enumerate(['A','B','C','D']):
    print i,val      # i xiabiao

print "-----------------"

for x,y in {(1,1),(2,4),(3,9),(4,16)}:
    print x,y

print "-----------------"

for a,b,c in {(-1,1,1.1),(-2,2,2.2),(-3,3,3.3)}:   # same type
    print a,b,c

