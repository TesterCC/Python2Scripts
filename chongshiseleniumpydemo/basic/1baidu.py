# coding=utf-8
"""
Selenium2 Python 自动化测试实战
P32
"""
from selenium import webdriver

driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver = webdriver.Ie()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()

driver.quit()