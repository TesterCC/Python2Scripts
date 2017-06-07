# !/usr/bin/env python
# coding: utf-8

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431679203477b5b364aeba8c4e05a9bd4ec1b32911e2000

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad Operand Type')
    if x >= 0:
        return x
    else:
        return -x

# print my_abs(-3)
# print my_abs(7)