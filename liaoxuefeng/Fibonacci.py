# coding:utf-8
'''
著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
'''

# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        # print b
        yield b
        print "Step:", b
        a,b =b, a+b
        n = n + 1

for n in fib(6):
    print n

# print fib(6)