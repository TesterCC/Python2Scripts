#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/8/29 13:14'

# http://www.jianshu.com/p/520749be7377
# python爬虫的最佳实践(五)--selenium+PhantomJS的简单使用


import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


class seleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()    # config phantomJS driver, PhantomJS，这是一个基于webkit的没有界面的浏览器

    def testEle(self):
        driver = self.driver
        driver.get('http://www.douyu.com/directory/all')
        soup = BeautifulSoup(driver.page_source, 'xml')     # 换了一种方式xml去获取到网页源码   原本的lxml
        while True:
            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})
            for title, num in zip(titles, nums):
                print title.get_text(), num.get_text()
            if driver.page_source.find('shark-pager-disable-next') != -1:
                break
            elem = driver.find_element_by_class_name('shark-pager-next')
            elem.click()
            soup = BeautifulSoup(driver.page_source, 'xml')

    def tearDown(self):
        print 'down'

if __name__ == "__main__":
    unittest.main()

