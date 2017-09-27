#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/27 00:38'

'''
Python 2.7 协程 gevent
https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001407503089986d175822da68d4d6685fbe849a0e0ca35000
'''

from gevent import monkey; monkey.patch_socket()
import gevent


def f(n):
    for i in range(n):
        # print gevent.getcurrent(), i # python2
        print("Current gevent: %s ===== Current i: %s" % (gevent.getcurrent(), i))  # compatible python2 python3
        gevent.sleep(0)   # 要让greenlet交替运行，可以通过gevent.sleep()交出控制权

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()