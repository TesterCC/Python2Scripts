#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 17:26'


import sys

from selenium.webdriver.common.by import By

from kaiyuanyouce.pagedemo.pages.basePage import Page

reload(sys)
sys.setdefaultencoding("utf-8")


# 百度搜索page
class SearchPage(Page):
    # 元素集
    # 搜索输入框
    search_input = (By.ID, u"kw")

    # 百度一下 按钮
    search_button = (By.ID, u"su")

    def __init__(self, driver, base_url=u"http://www.baidu.com"):
        Page.__init__(self, driver, base_url)

    def gotoBaiduHomePage(self):
        print(u"打开首页：%s" % self.base_url)
        self.driver.get(self.base_url)

    def input_search_text(self, text=u"渗透测试"):
        print(u"输入搜索关键字：%s" % text)
        self.input_text(self.search_input, text)

    def click_search_btn(self):
        print(u"点击 百度一下 按钮")
        self.click(self.search_button)
