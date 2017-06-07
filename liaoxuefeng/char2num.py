# coding:utf-8

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x*10+y

# 写出把str转换为int的函数
def char2num(s):
    return {'0':0, '1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

# print char2num('4')

print reduce(fn, map(char2num,'76543'))
print "----------------------"

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num,s))


print str2int('1237654')