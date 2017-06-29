#!/usr/bin/env python
# coding=utf-8
# 使用multiprocessing方式实现多进程 

import os

from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print 'Child process %s (%s) Running...' % (name, os.getpid())

if __name__ == '__main__':
    print "Parent process %s." % os.getpid()
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print "Process will start."
        p.start()