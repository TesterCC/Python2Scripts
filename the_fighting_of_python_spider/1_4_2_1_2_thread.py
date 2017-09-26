#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/26 05:11'

'''
Python爬虫开发与项目实战
1.4.2 多线程
1.2 从threading.Thread继承创建线程类  P23
'''

import random
import time
import threading


class myThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print("Current %s is running..." % threading.current_thread().name)
        for url in self.urls:
            print("%s ---->>> %s" % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)


print('%s is running ...' % threading.current_thread().name)

t1 = myThread(name="Thread_1", urls=['url_1', 'url_2', 'url_3'])
t2 = myThread(name="Thread_1", urls=['url_4', 'url_5', 'url_6'])

t1.start()
t2.start()
t1.join()
t2.join()   # 等待所有子进程执行完毕

print('%s ended.' % threading.current_thread().name)

