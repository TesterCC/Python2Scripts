# !/usr/bin/env python
# coding: utf-8

'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数
'''

import math


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')

    delta = b*b - 4*a*c
    if(delta < 0):
        print('此方程无解!')
    elif(delta == 0):
        x = (-b+delta)/(2*a)
        print('方程有两个相同的解!x1 = x2 = %.2f'%x)
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print('方程有两个不同的解!x1 = %.3f, x2 = %.2f'%(x1,x2))


print(quadratic(2, 3, 1))

print(quadratic(1, 3, -4))

