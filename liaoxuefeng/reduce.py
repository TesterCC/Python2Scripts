# coding:utf-8

'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00141861202544241651579c69d4399a9aa135afef28c44000
'''

def add(x,y):
    return x+y

print reduce(add, [1,2,3,4,5])

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x*10+y

print reduce(fn,[1,3,5,7,9])
print reduce(fn,[2,4,6])


print "-----------"


# 写出把str转换为int的函数
def char2num(s):
    return {'0':0, '1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print char2num('4')

print reduce(fn, map(char2num,'13579'))