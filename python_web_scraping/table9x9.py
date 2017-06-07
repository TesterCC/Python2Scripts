#!/usr/bin/env python
# coding:utf-8


'''
python网络爬虫实战--胡松涛
P78-79   九九乘法表
'''

class PrintTable(object):
    '''
    打印九九乘法表
    '''
    def __init__(self):
        print(u'开始打印9x9乘法表')
        self.print99()


    def print99(self):
        for i in range(1,10):
            for j in range(1, i+1):
                print('%dX%d=%2s\t' % (j, i, j*i))
            print('\n')


if __name__ == '__main__':
    pt = PrintTable()
