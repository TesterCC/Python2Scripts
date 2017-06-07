# coding:utf-8

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(1)
print fact(2)
print fact(3)
print fact(10)
print fact(1000)

# 使用递归函数需要注意防止栈溢出
# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00137473836826348026db722d9435483fa38c137b7e685000