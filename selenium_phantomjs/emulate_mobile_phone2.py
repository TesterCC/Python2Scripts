#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/8/31 18:32'

# http://blog.csdn.net/max229max/article/details/70807918
# Python - Selenium Chrome

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mobile_emulation = {'deviceName': 'iPhone 6'}

# complex mode
# mobile_emulation = {
#     "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
#     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
# }

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(chrome_options= chrome_options)
driver.get("http://www.baidu.com")

time.sleep(3)

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()