#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/5 04:28'


'''
P81-82
python网络爬虫实战--胡松涛

将理想状态绝对无误差的10个同样的小球从1-10标号，然后随机从中选出1个小球。
如果选取的次数足够多，就可以计算各个小球被选取出来的概率。
'''

import random


class SelectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = raw_input('输入测试的次数：')
            try:
                num = int(numStr)
            except ValueError:
                print(u"要求输入一个整数")
                continue
            else:
                break

        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # 对应1-10号球出现的次数
        for i in xrange(num):
            n = random.randint(1, 10)
            # print n
            ball[n-1] += 1   # index 从0开始计数
            # print ball

        for i in xrange(1, 11):
            print(u"获取第%d号球的概率为%f" % (i, ball[i-1]*1.0/num))

if __name__ == '__main__':
    SB = SelectBall()