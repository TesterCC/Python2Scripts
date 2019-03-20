#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-20 11:55'


"""
高效开发 红书 P236   

使用Tornado协程可以开发出类似同步代码的异步行为
因为协程本身不使用现成，所以减少了线程上下文切换的开销

REF:
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000
"""

# use coroutine achieve website visit function

from tornado import gen      # 引入协程库
from tornado.httpclient import AsyncHTTPClient

