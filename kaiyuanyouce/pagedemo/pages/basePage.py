#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 17:26'


import sys

reload(sys)
sys.setdefaultencoding("utf-8")


# pages basic class
class Page(object):
    """
       Page基类，所有page都应该继承该类
    """

    def __init__(self, driver, base_url=u"http://www.baidu.com"):
        self.driver = driver
        self.base_url = base_url
        self.timemout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title