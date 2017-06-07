# coding: utf-8

'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819873910807d8c322ca74d269c9f80f747330a52000
'''

def add(x,y,f):
    return f(x)+f(y)


print add(-7,-1,abs)