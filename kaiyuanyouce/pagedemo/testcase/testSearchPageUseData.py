#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 21:05'

import unittest
import sys
from time import sleep

import xlrd
from selenium import webdriver

from kaiyuanyouce.pagedemo.common import HTMLTestRunner
from kaiyuanyouce.pagedemo.pages.searchPage import SearchPage

reload(sys)
sys.setdefaultencoding("utf-8")

'''
参考testSearchPage.py和read_excel_demo.py进行组装
'''


# 可以考虑单独列一个工具类
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


# 百度搜索测试
class TestSearchPageUseData(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()     # choose a browser driver
        self.driver.implicitly_wait(30)    # 给当前webdriver设置全局隐性等待时间，最大30s
        self.base_url = u"http://www.baidu.com"  # 设置首页url
        # self.path = u"../res/baidu_search.xls"   # ../  表示相对路径 本文件debug运行路径
        self.path = u"../pagedemo/res/baidu_search.xls"   # ../  表示相对路径 在main.py文件运行路径

    def testSearch(self):
        driver = self.driver
        print(u"开始[case_0001]百度搜索")

        # load test data
        test_excel = LoadBaiduSearchTestData(self.path)
        data = test_excel.load_data()
        print(data)

        # 循环参数化
        for d in data:
            # 打开百度首页
            search_Page = SearchPage(driver, self.base_url)

            # 启动浏览器，访问百度首页
            search_Page.gotoBaiduHomePage()

            # 输入 搜索词 , 参数化 搜索词
            search_Page.input_search_text(d[1])  # text可变

            # 单击 百度一下 按钮进行搜索
            search_Page.click_search_btn()
            sleep(2)
            # 验证标题
            self.assertEqual(search_Page.get_title(), d[2])  # assert_title可变
            sleep(1)

    def tearDown(self):
        self.driver.quit()


# 可注释，just for test
# if __name__ == '__main__':
#     testunit = unittest.TestSuite()
#     testunit.addTest(TestSearchPageUseData('testSearch'))
#
#     # 定义报告输出路径
#     htmlPath = u"testReport.html"
#     fp = file(htmlPath, "wb")
#
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                            title=u"百度测试",
#                                            description=u"测试用例结果")
#     runner.run(testunit)
#
#     fp.close()