#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/27 00:38'

'''
Python 2.7 协程 gevent
https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001407503089986d175822da68d4d6685fbe849a0e0ca35000

实际代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换
'''

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2


def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])