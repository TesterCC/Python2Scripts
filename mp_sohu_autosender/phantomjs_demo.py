#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/10 16:58'

from selenium import webdriver
from time import sleep

"""
http://phantomjs.org/download.html
for download phantomjs browser driver
phantomjs -v
2.1.1
"""
driver = webdriver.PhantomJS()

driver.get('http://phantomjs.org/download.html')

sleep(3)
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)

driver.quit()

