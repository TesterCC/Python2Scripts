# coding:utf-8

'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868196435255fcca20a1630446ea2dd434a7176e152000
'''

# d = {'a':1, 'b':2, 'c':3}
# for key in d:
#     print key

d = {'a':1, 'b':2, 'c':3, 'd':4}

for key in d.iterkeys():
    print key

print "-----------"

for val in d.itervalues():
    print val
print "-----------"

for item in d.iteritems():
    print item
print "-----------"


for ch in 'ABCDEFG':
    print ch

