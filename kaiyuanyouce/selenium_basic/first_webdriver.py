#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/18 21:07'


'''
To test webdriver

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247483731&idx=1&sn=00aeb78030de3e8c6f041bd8fef650dc&scene=19#wechat_redirect
'''

import sys
from time import sleep

from selenium import webdriver
import unittest
import HTMLTestRunner

reload(sys)
sys.setdefaultencoding("utf-8")   # 设置当前python运行在utf-8编码下，这样你的中文就不会乱码了


class BaiduTest(unittest.TestCase):
    """百度首页搜索测试用例"""

    # 用例级初始化函数，自动执行
    def setUp(self):
        self.driver = webdriver.Chrome()       # 初始化基于Chrome浏览器的webdriver实例
        self.driver.implicitly_wait(30)        # 给当前webdriver设置全局隐性等待时间，最大30s
        self.base_url = u"http://www.baidu.com"    # 设置首页url

    def test_baidu_search(self):
        driver = self.driver         # 简单赋值，这样在本测试中后续就不用每次都写self.driver,而是写driver
        print u"开始[case_0001]百度搜索"   # 在控制台打印输出, 也可以import logging打印到日志文件中
        driver.get(self.base_url)    # 启动浏览器，并访问首页

        # verify title
        self.assertEqual(driver.title, u"百度一下，你就知道")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"开源优测")
        driver.find_element_by_id("su").click()   # 单击 百度一下  按钮
        sleep(3)

        # verify search result title
        self.assertEqual(driver.title, u"开源优测_百度搜索")

    # 用例级清理函数，自动执行
    def tearDown(self):
        self.driver.quit()    # 退出webdriver，同时关闭当前webdrier session下所有浏览器窗口

# python main函数
if __name__ == '__main__':
    testunit = unittest.TestSuite()     # 初始化一个用例套件集
    testunit.addTest(BaiduTest('test_baidu_search'))    # 往用例套件集新增一个测试

    # 定义报告输出路径，这里是当前目录
    htmlPath = u"testReport.html"
    fp = file(htmlPath, 'wb')

    # 构建一个HTMLTestReport执行器
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试", description=u"测试用例结果")

    # 运行测试集
    runner.run(testunit)    # main 1st line

    # 关闭打开的测试报告文件
    fp.close()




