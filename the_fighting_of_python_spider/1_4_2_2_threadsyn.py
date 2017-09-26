#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/26 05:46'

'''
Python爬虫开发与项目实战
1.4.2 多线程
2 线程同步  P24
'''

import threading

mylock = threading.RLock()   # 允许一个线程多次对其进行acquire操作
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print("%s locked, Number: %d" % (threading.current_thread().name, num))
            if num >= 4:
                mylock.release()
                print("%s released, Number: %d" % (threading.current_thread().name, num))
                break
            num += 1
            print("%s released, Number: %d" % (threading.current_thread().name, num))
            mylock.release()


if __name__ == '__main__':
    thread1 = myThread('Thread_1')
    thread2 = myThread('Thread_2')
    thread1.start()
    thread2.start()