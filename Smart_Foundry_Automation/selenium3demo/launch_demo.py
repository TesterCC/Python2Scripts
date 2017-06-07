#!/usr/bin/env python
# coding:utf-8

from selenium import webdriver

chrome_path = "/Users/TesterCC/Development/webdriver/chromedriver"

firefox_path = "/Users/TesterCC/Development/webdriver/geckodriver"

safari_path = "/usr/bin/safaridriver"

driver = webdriver.Chrome(chrome_path)  # use webdriver.Firefox() have some trouble,this method can launch firefox

# driver = webdriver.Chrome(safari_path)

driver.get("https://developer.smartfoundry.io/")

driver.maximize_window()


driver.quit()




