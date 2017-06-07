# coding:utf-8

'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681963899940a998c0ace64bb5ad45d1b56b103c48000
列表生成式

'''


# generate 1 to 10 list
print range(1,11)
print "------------------------"

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print [x*x for x in range(1,11)]
print "------------------------"
print [x*x for x in range(1,11) if x%2==0] # 仅偶数的平方
print "------------------------"
print [x*x for x in range(1,11) if x%2==1]  # 仅奇数的平方
print "------------------------"

# 还可以使用两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print "------------------------"

# 同上
L = []
for m in 'ABC':
    for n in 'XYZ':
        L.append(m+n)
print L
print "------------------------"

print [a+b+c for a in 'ABC' for b in 'XYZ' for c in 'OPQ']   # left to right, outer to inner
print "------------------------"





