#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 17:27'

import unittest
import sys
from time import sleep

from selenium import webdriver

from kaiyuanyouce.pagedemo.pages.searchPage import SearchPage

reload(sys)
sys.setdefaultencoding("utf-8")


# 百度搜索测试
class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()      # choose a browser driver

    def testSearch(self):
        driver = self.driver
        # Baidu URL
        url = u"http://www.baidu.com"
        text = u"渗透测试"
        # 期望验证的标题
        assert_title = u"渗透测试_百度搜索"
        print(assert_title)

        search_Page = SearchPage(driver, url)

        # 启动浏览器，访问百度首页
        search_Page.gotoBaiduHomePage()

        # 输入 搜索词
        search_Page.input_search_text(text)    # text可变

        # 单击 百度一下 按钮进行搜索
        search_Page.click_search_btn()
        sleep(2)
        # 验证标题
        self.assertEqual(search_Page.get_title(), assert_title)   # assert_title可变

    def tearDown(self):
        self.driver.quit()