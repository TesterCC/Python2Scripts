#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/8/31 18:14'


# https://mp.weixin.qq.com/s?__biz=MzI0MTAzNjYzMw==&mid=2652680354&idx=1&sn=85caf0d37bcaffb1afb6f63499c37d4f&chksm=f2f9ac94c58e25820e1ca7d9a87325bd7288c1501b87d16a45ce4445ba3bfbb6ec24fb233e60&mpshare=1&scene=23&srcid=0825jxTb24bWPYw7sXuQiCpC#rd

# python+chrome+Selenium模拟手机浏览器

from time import sleep

from selenium import webdriver


# setting emulate phone

mobile_emulation = {'deviceName': 'Nexus 5X'}

options = webdriver.ChromeOptions()

options.add_experimental_option('mobileEmulation', mobile_emulation)

# launch driver

driver = webdriver.Chrome(chrome_options=options)

# visit baid wap page
driver.get("http://m.baidu.com")

sleep(3)

print(driver.title)
print(driver.current_url)
print(driver.page_source)


driver.quit()