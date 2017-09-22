#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 15:52'

'''
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247483732&idx=1&sn=3ae63248f6ceeffa9b3c71012e83686e&scene=19#wechat_redirect

如何利用xlrd来实现python selenium2自动化测试参数化
'''

from time import sleep
import sys
import unittest

from selenium import webdriver
import HTMLTestRunner
import xlrd

reload(sys)
sys.setdefaultencoding("utf-8")


class LoadBaiduSearchTestData(object):
    def __init__(self, path):
        self.path = path

    def load_data(self):
        # open excel file
        excel = xlrd.open_workbook(self.path)

        # get 1st work sheet
        table = excel.sheets()[0]

        # get row number
        nrows = table.nrows

        # 从第二行开始遍历数据
        # 存入一个list中
        test_data = []
        for i in range(1, nrows):
            test_data.append(table.row_values(i))

        # return read data list
        return test_data


class BaiduTest(unittest.TestCase):
    """百度首页搜索测试用例"""

    def setUp(self):
        self.driver = webdriver.Chrome()  # 初始化基于Chrome浏览器的webdriver实例
        self.driver.implicitly_wait(30)  # 给当前webdriver设置全局隐性等待时间，最大30s
        self.base_url = u"http://www.baidu.com"  # 设置首页url
        self.path = u"baidu_search.xls"

    def test_baidu_search(self):
        driver = self.driver
        print(u"开始[case_0001]百度搜索")

        # load test data
        test_excel = LoadBaiduSearchTestData(self.path)
        data = test_excel.load_data()
        print(data)

        # 循环参数化
        for d in data:
            # 打开百度首页
            driver.get(self.base_url)
            # 验证标题
            self.assertEqual(driver.title, u"百度一下，你就知道")
            sleep(1)

            driver.find_element_by_id("kw").clear()
            # 参数化 搜索词
            driver.find_element_by_id("kw").send_keys(d[1])
            sleep(1)
            driver.find_element_by_id("su").click()
            sleep(1)
            # 参数化 验证搜索结果标题
            self.assertEqual(driver.title, d[2])
            sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(BaiduTest('test_baidu_search'))

    # 定义报告输出路径
    htmlPath = u"testReport.html"
    fp = file(htmlPath, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"百度测试",
                                           description=u"测试用例结果")
    runner.run(testunit)

    fp.close()





