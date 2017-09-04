#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/2 17:08'

'''
python网络爬虫实战--胡松涛
P59-64

编写一个简单的程序makePasswordFileFunction.py,创建一个有针对性的专用密码字典。

根据用户输入的密码元素来创建一个字典列表
'''


import os
import platform
import itertools
import time


class MakePassword(object):
    def __init__(self):
        self.rawList = []
        self.denyList = ['', ' ', '@']
        self.pwdList = []
        self.minLen = 6
        self.maxLen = 16
        self.timeout = 3
        self.flag = 0
        self.run = {
            '0': exit,
            '1': self.getRawList,
            '2': self.addDenyList,
            '3': self.clearRawList,
            '4': self.setRawList,
            '5': self.modifyPasswordList,
            '6': self.createPasswordList,
            '7': self.showPassword,
            '8': self.createPassowrdFile
        }
        self.main()

    def main(self):
        '''主程序'''
        while True:
            self.mainMenu()
            op = raw_input("请输入选项: ")
            if op in map(str, range(len(self.run))):
                self.run.get(op)()
            else:
                self.tipMainMenuInputError()
                continue

    def mainMenu(self):
        '''主菜单'''
        self.clear()
        print(u"||"),
        print(u"="*40),
        print(u"||")
        print(u"|| O: 退出程序")
        print(u"|| 1: 输入密码原始字符串")
        print(u"|| 2: 添加非法字符到列表")
        print(u"|| 3: 清空原始密码列表")
        print(u"|| 4: 整理原始密码列表")
        print(u"|| 5: 改变默认密码长度(%d-%d)" % (self.minLen, self.maxLen))
        print(u"|| 6: 创建密码列表")
        print(u"|| 7: 显示所有密码")
        print(u"|| 8: 创建字典文件")
        print(u"||"),
        print(u"=" * 40),
        print(u"||")
        print(u"当前非法字符为: %s" % self.denyList)
        print(u"当前原始密码元素为: %s" % self.rawList)
        print(u"共有密码%d个" % len(self.pwList))

        if self.flag:
            print(u"已在当前目录创建密码文件dic.txt")
        else:
            print(u"尚未创建密码文件")

    def clear(self):
        '''清屏函数'''
        OS = platform.system()
        if OS == u"Windows":
            os.system('cls')
        else:
            os.system('clear')

    def tipMainMenuInputError(self):
        '''错误提示'''
        self.clear()
        print(u"只能输入0-7的整数，等待%d秒后重新输入" % timeout)
        time.sleep(time.out)

    def getRawList(self):
        '''获取原始数据列表'''
        self.clear()
        print(u"输入回车后直接退出")
        print(u"当前原始密码列表为: %s" % self.rawList)
        st = None
        while not st == '':
            st = raw_input("请输入密码元素字符串：")
            if st in self.denyList:
                print(u"这个字符串是预先设定的非法字符串")
                continue
            else:
                self.rawList.append(st)
                self.clear()
                print(u"输入回车后直接退出")
                print(u"当前原始密码列表为：%s" % self.rawList)

    def addDenyList(self):
        '''添加非法词'''
        self.clear()
        print(u"输入回车后直接退出")
        print(u"当前非法字符为：%s" % self.denyList)
        st = None
        while not st == '':
            st = raw_input(u"请输入需要添加的非法字符串：")
            self.denyList.append(st)
            self.clear()
            print(u"输入回车后直接退出")
            print(u"当前非法字符列表为：%s" % self.denyList)

    def clearRawList(self):
        '''清空原始数据库列表'''
        self.rawList = []

    def setRawList(self):
        '''整理原始数据列表'''
        a = set(self.rawList)
        b = set(self.denyList)
        self.rawList = []
        for str in set(a - b):
            self.rawList.append(str)

    def modifyPasswordLen(self):
        '''修改默认密码的长度'''
        self.clear()

        while True:
            print(u"当前密码长度为%d-%d" % (self.minLen, self.maxLen))
            min = raw_input(u"请输入密码最小长度:")
            max = raw_input(u"请输入密码最大长度:")
            try:
                self.minLen = int(min)
                self.maxLen = int(max)
            except ValueError:
                print(u"密码长度只能输入数字[6-18]")
                break
            if self.minLen not in xrange(6, 19) or self.maxLen not in xrange(6, 19):
                print(u"密码长度只能输入数字[6-18]")
                self.minLen = 6
                self.maxLen = 16
                continue
            if self.minLen == self.maxLen:
                res = raw_input(u"请确定将密码长度设定为%d吗?(Yy/Nn)" % self.minLen)
                if res not in list('YyNn'):
                    print(u"输入错误，请重新输入")
                    continue
                elif res in list('Yy'):
                    print(u"好吧，你确定就好")
                    break
                else:
                    print(u"给个机会，改一下吧")
                    continue
            elif self.minLen > self.maxLen:
                print(u"最小长度比最大长度还大，可能吗？请重新输入")
                self.minLen = 6
                self.maxLen = 16
                continue
            else:
                print(u"设置完毕，等待％d秒后回主菜单" % self.timeout)
                time.sleep(self.timeout)
                break

    def createPasswordList(self):
        '''创建密码列表'''
        titleList = []
        swapcaseList = []
        for st in self.rawList:
            swapcaseList.append(st.swapcase())  # swapCase()对字符串的大小写字母进行转换，大转小，小转大
            titleList.append(st.title())  # 所有单词都是以大写开始，其余字母均为小写
        sub1 = []
        sub2 = []
        for st in set(self.rawList + titleList + swapcaseList):
            sub1.append(st)
        for i in xrange(2, len(sub1) + 1):
            sub2 += list(itertools.permutations(sub1, i))  # 实现排列组合
        for tup in sub2:
            PW = ''
            for subPW in tup:
                PW += subPW
            if len(PW) in xrange(self.minLen, self.maxLen + 1):
                self.pwList.append(PW)
            else:
                pass

    def showPassword(self):
        '''显示创建的密码'''
        for i in xrange(len(self.pwList)):
            if i % 4 == 0:
                print("%s\n" % self.pwList[i])
            else:
                print("%s\n" % self.pwList[i]),
        print('\n')
        print(u"显示%d秒，回到主菜单" % self.timeout)
        time.sleep(self.timeout)

    def createPasswordFile(self):
        '''创建密码字典文件'''
        print(u"当前目录下创建字典文件：dic.txt")
        time.sleep(self.timeout)
        with open('./dic.txt', 'w+') as fp:
            for PW in self.pwList:
                fp.write(PW)
                fp.write("\n")
        self.flag = 1


if __name__ == '__main__':
    mp = MakePassword()

    # 有bug，无法正常生成字典文件