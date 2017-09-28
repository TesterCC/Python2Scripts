#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/28 11:24'

'''
Python爬虫开发与项目实战
1.4.4 分布式进程
Linux服务器进程
P28-29

不理解的话可以参考：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000
'''

import random,time,Queue

from multiprocessing.managers import BaseManager

# 第一步：建立task_queue和result_queue, 用来存放任务和结果
# 发送任务的队列
task_queue = Queue.Queue()
# 接收结果的队列
result_queue = Queue.Queue()


# 从BaseManager继承的QueueManager
class Queuemanager(BaseManager):
    pass


# 第二步：把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象
# 将Queue对象在网络中暴露(把两个Queue都注册到网络上, callable参数关联了Queue对象)
Queuemanager.register('get_task_queue', callable=lambda: task_queue)
Queuemanager.register('get_result_queue', callable=lambda: result_queue)

# 第三步：绑定端口8001，设置验证口令'pentest'。相当于对象的初始化
manager = Queuemanager(address=('', 8001), authkey='pentest')

# 第四步：启动管理，监听信息通道。
manager.start()

# 第五步：通过管理实例的方法 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 第六步：添加任务
for url in ["ImageUrl_" + str(i) for i in range(10)]:
    print("put task %s ..." % url)
    task.put(url)

# 获取返回结果 从result队列读取结果
print("Try get result ...")
for i in range(10):
    try:
        print("Result is %s" % result.get(timeout=10))
    except Queue.Empty:
        print('task queue is empty.')

# 关闭管理
manager.shutdown()

print('master exit.')