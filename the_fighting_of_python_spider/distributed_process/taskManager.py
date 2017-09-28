#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/28 11:24'

'''
Python爬虫开发与项目实战
1.4.4 分布式进程
Linux服务器进程
P28-29
'''

import random,time,Queue

from multiprocessing.managers import BaseManager

# 第一步：建立task_queue和result_queue, 用来存放任务和结果
task_queue = Queue.Queue()
result_queue = Queue.Queue()

class Queuemanager(BaseManager):
    pass

# 第二步：把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象
# 将Queue对象在网络中暴露
Queuemanager.register('get_task_queue', callable=lambda:task_queue)
Queuemanager.register('get_result_queue', callable=lambda:result_queue)

# 第三步：绑定端口8001，设置验证口令'test'。相当于对象的初始化
