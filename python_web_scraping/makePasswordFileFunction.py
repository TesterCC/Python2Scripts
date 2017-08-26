#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/8/25 17:41'

'''
python网络爬虫实战--胡松涛
P53-58

编写一个简单的程序makePasswordFileFunction.py,创建一个有针对性的专用密码字典。

'''

import os
import platform
import itertools
import time


def main():
    '''主程序'''
    global rawList   # Initial data list
    rawList = []
    global denyList  # illegal words list
    denyList = [' ', '', '@']
    global pwList    # final password list
    pwList = []
    global minLen    # minimum length of password
    minLen = 6
    global maxLen    # maximum length of password
    maxLen = 16
    global timeout
    timeout = 3
    global flag
    flag = 0
    run = {
        '0': exit,   # exit
        '1': getRawList,    # createRawList
        '2': addDenyList,
        '3': clearRawList,
        '4': setRawList,
        '5': modifyPasswordLen,
        '6': createPasswordList,    # 创建最终的字典列表
        '7': showPassword,
        '8': createPasswordfile
    }

    while True:
        mainMenu()
        op = raw_input("请输入选项: ")
        if op in map(str, range(len(run))):
            run.get(op)()
        else:
            tipMainMenuInputError()
            continue


def mainMenu():
    '''主菜单'''
    global DenyList
    global rawList
    global pwList
    global flag
    clear()
    print(u"||"),
    print(u"="*40),
    print(u"||")
    print(u"|| 0: 退出程序")
    print(u"|| 1: 输入密码原始字符串")
    print(u"|| 2: 添加非法字符到列表")
    print(u"|| 3: 清空原始密码列表")
    print(u"|| 4: 整理原始密码列表")
    print(u"|| 5: 改变默认密码长度(%d-%d)" % (minLen, maxLen))
    print(u"|| 6: 创建密码列表")
    print(u"|| 7: 显示所有密码")
    print(u"|| 8: 创建字典文件")
    print(u"||")
    print(u"||"),
    print(u"=" * 40),
    print(u"||")
    print(u"当前非法字符为: %s" % denyList)
    print(u"当前原始密码元素为: %s" % rawList)
    print(u"共有密码%d个" % len(pwList))

    if flag:
        print(u"已在当前目录创建密码文件dic.txt")
    else:
        print(u"尚未创建密码文件")


def clear():
    '''清屏函数'''
    os = platform.system()
    if (os == u"Windows"):
        os.system('cls')
    else:
        os.system('clear')


def tipMainMenuInputError():
    pass


def getRawList():
    pass

def addDenyList():
    pass

def clearRawList():
    pass

def setRawList():
    pass
def modifyPasswordLen():
    pass

def createPasswordList():
    pass

def showPassword():
    pass

def createPasswordfile():
    pass