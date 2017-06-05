#!/usr/bin/env python
# coding:utf-8


def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

enroll('Lily', 'F')


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2, 3, 4)
print calc()

nums = [1, 2, 3]
print calc(nums[0], nums[1], nums[2])


# 关键字参数