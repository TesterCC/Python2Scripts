# coding:utf-8
'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681965108490cb4c13182e472f8d87830f13be6e88000
'''


L = [x*x for x in range(10)]
print L
print "---------------------------------"
g = (x*x for x in range(10))
print g
# print g.next()
# print g.next()
# print g.next()

for n in g:
    print n

