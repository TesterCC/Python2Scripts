#!/usr/bin/env python
# coding:utf-8

# filter()删除1~100的素数

from math import sqrt


def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return True
    return False


print filter(is_prime, range(1,101))