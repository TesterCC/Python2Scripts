# coding:utf-8

'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
'''

L = [2,4,6,10]

def prod(x,y):
    return x*y

print reduce(prod,L)

print reduce(lambda x,y:x*y, L)

print reduce(lambda x,y:x*y, [1,3,5,10])

