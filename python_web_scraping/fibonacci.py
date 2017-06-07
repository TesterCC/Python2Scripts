#!/usr/bin/env python
# coding:utf-8

'''
python网络爬虫实战--胡松涛
P81-80    求斐波那契数列  0，1，1，2，3，5，8，13，32...
'''

class Fibonacci(object):
    '''Return a Fibonacci Sequence'''
    def __init__(self):
        self.fList = [0, 1]  # set initial list
        self.main()

    def main(self):
        listLen = raw_input('请输入fibonacci数列的长度(3-50):')
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print('得到的fibonacci数列为:\n %s ' % self.fList)


    def checkLen(self, lenth):  #检查输入的数据是否符合要求
        lenList = map(str, range(3,51))     # str, int transfer to str
        if lenth in lenList:
            print(u'输入的长度符合标准，继续运行')
        else:
            print(u'只能输入3-50,太长了不是不能算，只是这里没有必要')
            exit()

if __name__ == '__main__':
    f = Fibonacci()