#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/26 05:11'

'''
Python爬虫开发与项目实战
1.4.2 多线程
1.1 用threading模块创建多线程  P22
'''

import random
import time
import threading


# 新线程执行代码
def thread_run(urls):
    print('Current %s is runing ...' % threading.current_thread().name)
    for url in urls:
        print("%s---->>> %s" % (threading.current_thread().name, url))
        time.sleep(random.random())
    print("%s ended." % threading.current_thread().name)


print('%s is running ...' % threading.current_thread().name)

t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1', 'url_2', 'url_3'],))
t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url_4', 'url_5', 'url_6'],))

t1.start()
t2.start()
t1.join()
t2.join()   # 等待所有子进程执行完毕

print('%s ended.' % threading.current_thread().name)

