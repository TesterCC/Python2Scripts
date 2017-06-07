#!/usr/bin/env python
# coding:utf-8

'''
http://baike.baidu.com/link?url=604_R07UK-8IezKl8aL_gPWbB7NW7Blv1_5SJeTsVlQvUdQ9weJxms2eB2kISPjCrumYSpYhlX9SoCqNQefud_MKarGikPnhTg0KtGYxV0ZNaF7vnP2Fdi_j5XD61do_a2rX_yp7i-L9E5PIn-UHVobre_Hh1hZL9QYfVR6uZbi
'''

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


print filter(is_prime, range(1,11))   # find prime in list