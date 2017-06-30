#!/usr/bin/env python
# coding=utf-8

'''
4-3-1 比较合并排序和快速排序
算法图解 P66
'''

voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick it out!")
    else:
        voted[name] = True
        print("Let it vote.")

if __name__ == '__main__':
    check_voter("Tom")
    check_voter("Jim")
    check_voter("Tom")
    check_voter("Lisa")
