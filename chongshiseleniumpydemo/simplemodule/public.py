#!/usr/bin/env python
# coding:utf-8

# Encapsulate public action

username = "yanxi";
password = "yanxi76543210"
baseurl = "http://intranet.gnum.com/wp-login.php"

def login(driver):
    driver.find_element_by_id("user_login").clear();
    driver.find_element_by_id("user_login").send_keys(username)
    driver.find_element_by_id("user_pass").clear();
    driver.find_element_by_id("user_pass").send_keys(password)
    driver.find_element_by_id("wp-submit").click()

#Logout Action
def logout(driver):
    # driver.find_element(u"").click()
    driver.quit()