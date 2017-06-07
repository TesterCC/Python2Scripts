# !/usr/bin/env python
# coding: utf-8
# P71-72  4.2.2 控制浏览器后退前进

from selenium import webdriver

driver = webdriver.Firefox()

# visit baidu homepage
first_url = 'http://www.baidu.com'
print "now access %s" %(first_url)
driver.get(first_url)

# visit news page
second_url = 'http://news.baidu.com'
print "now access %s" %(second_url)
driver.get(second_url)

# back to baidu homepage
print "Back to %s " % (first_url)
driver.back()

# forward to news page
print "Forward to %s" % (second_url)
driver.forward()

driver.quit()
