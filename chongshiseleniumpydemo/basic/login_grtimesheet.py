#!/usr/bin/env python
# coding:utf-8
# 模块化实例

from selenium import webdriver

username = "yanxi";
password = "yanxi76543210"
baseurl = "http://intranet.gnum.com/wp-login.php"

#Login Action
def login():
    driver.find_element_by_id("user_login").clear();
    driver.find_element_by_id("user_login").send_keys(username)
    driver.find_element_by_id("user_pass").clear();
    driver.find_element_by_id("user_pass").send_keys(password)
    driver.find_element_by_id("wp-submit").click()

#Logout Action
def logout():
    # driver.find_element(u"退出").click()
    driver.quit()


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(baseurl)
login()

# click,edit etc.

logout()