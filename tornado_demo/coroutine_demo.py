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

@gen.coroutine    # 使用装饰器声明这是一个协程函数
def coroutine_visit():
    http_client = AsyncHTTPClient()
    # yield的使用使得代码中不用再编写回调函数用于处理访问结果，而是直接在yield语句的后面写结果处理语句
    response = yield http_client.fetch("www.baidu.com")
    print(response.body)


'''
协程函数的3种调用方式
1.本身是协程的函数内通过yield关键字调用
2.在IOLoop未启动时，通过IOLoop的run_sync()函数调用
3.在IOLoop已启动时，通过IOLoop的spawn_callback()函数调用

IOLoop是Tornado的主事件循环对象，Tornado程序通过它监听外部客户端的访问请求，并执行相应操作。
'''

# 通过协程函数调用协程函数
def outer_coroutine():   # outer_coroutine()也是协程函数
    print("start call another coroutine")
    yield coroutine_visit()   # 1.本身是协程的函数内通过yield关键字调用
    print("end of outer_coroutine")

# print(outer_coroutine())

# 当程序尚未进入IOLoop的running状态,可通过run_sync()函数调用协程函数

from tornado.ioloop import IOLoop