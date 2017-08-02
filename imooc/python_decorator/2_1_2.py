#!/usr/bin/env python
#coding=utf-8


'''
http://www.imooc.com/video/10832
2-1 python装饰器之闭包1 after 05:56
'''

# complex, redundancy
# def func_150(val):
#     passline = 90   # total score 150, priority
#     if val >= passline:
#         print ('pass')
#     else:
#         print ('failed')
#
#
# def func_100(val):
#     passline = 60   # total score 150, priority
#     if val >= passline:
#         print ('pass')
#     else:
#         print ('failed')


# simple
def set_passline(passline):  # passline = 60
    def cmp(val):    # passline is add in __closure__
        if val >= passline:
            print("Pass")
        else:
            print('Failed')
    return cmp

if __name__ == '__main__':

    # func_150(89)
    # func_100(89)
    f_100 = set_passline(60)
    # print(type(f_100))
    # print(f_100.__closure__)
    f_150 = set_passline(90)
    f_100(89)
    f_150(89)
