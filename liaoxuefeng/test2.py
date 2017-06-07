# !/usr/bin/env python
# coding: utf-8

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431679203477b5b364aeba8c4e05a9bd4ec1b32911e2000
# 返回多个值

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100,100,60,math.pi/6)
print (x, y)

r = move(100,100,60,math.pi/6)
print r
