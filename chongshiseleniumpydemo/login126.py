# !/usr/bin/env python
# coding: utf-8
# P72-73  4.3.1 126邮箱登录

# change to login wordpress

from selenium import webdriver
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

login_url = "http://intranet.gnum.com/wp-login.php"
driver.get(login_url)
time.sleep(3)

input_username = driver.find_element_by_id("user_login")
input_password = driver.find_element_by_id("user_pass")
submit_btn = driver.find_element_by_id("wp-submit")

input_username.clear()
input_username.send_keys("yanxi")

input_password.clear()
input_password.send_keys("yanxi76543210")

submit_btn.click()

time.sleep(3)

def GetNowTime():
    '''
    The function of method : get current time
    :return:
    '''
    return time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))

# 2016-10-09 17:28:02       %Y-%m-%d %H:%M:%S
# 20161009 172802     %Y%m%d_%H%M%S

screenshot_save_path = "E:\\wordpress_test\\"+GetNowTime()+".jpg"

print("Screenshot save path is :"+screenshot_save_path)

driver.get_screenshot_as_file(screenshot_save_path)

driver.quit()
