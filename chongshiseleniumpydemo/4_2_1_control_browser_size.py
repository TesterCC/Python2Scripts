# !/usr/bin/env python
# coding: utf-8
# P71 4.2.1 控制浏览器窗口大小
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://m.mail.10086.cn")

# 参数数字为像素点
print "设置浏览器宽480，高800显示"
driver.set_window_size(480,800)
driver.maximize_window()
driver.set_window_size(600,600)
driver.maximize_window()
driver.quit()