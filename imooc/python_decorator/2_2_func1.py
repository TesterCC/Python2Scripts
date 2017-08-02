#!/usr/bin/env python
#coding=utf-8


'''
http://www.imooc.com/video/10833
2-2 python装饰器之闭包2
'''


# 两者都是可变参数，当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值。
# *args表示任何多个无名参数，它是一个tuple
# **kwargs表示关键字参数，它是一个dict


def my_sum(*arg):
    # if len(arg) == 0:
    #     return 0
    # for val in arg:
    #     if not isinstance(val, int):
    #         return 0
    print('in my_sum')
    return sum(arg)


def my_average(*arg):
    # if len(arg) == 0:
    #     return 0
    # for val in arg:
    #     if not isinstance(val, int):
    #         return 0
    return sum(arg)/len(arg)


def dec(func):
    def in_dec(*arg):     # my_sum放到enclosure属性中 # then my_sum = in_dec(*arg)
        print("in dec arg=", arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)    # end of in_dec()
    return in_dec    # end of dec ()


# first call dec(), then return in_dec -> func my_sum
# then my_sum = in_dec(*arg)
my_sum = dec(my_sum)

print(my_sum(1, 2, 3, 4, 5))
print(my_sum(1, 2, 3, 4, 5, '6'))

my_average = dec(my_average)

print(my_average(1, 2, 3, 4, 5))
print(my_average(1, 2, 3, 4, 5, '6'))