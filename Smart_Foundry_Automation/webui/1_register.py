#!/usr/bin/env python
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time


# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# setting browser weight 600, height 800
# driver.set_window_size(600,800)

target_url = "https://staging.smartfoundry.io"
#target_url = "172.27.1.85"

driver.get(target_url)
# driver.implicitly_wait(7)

time.sleep(3)

# window maximize
driver.maximize_window()

# header
# header = driver.find_element_by_xpath("html/body/header/div/div/ul")

# class="sf-mainmenu"


# got_it = driver.find_element_by_xpath("html/body/footer/div/div/div[2]/div/div[2]")
# got_it.click()

time.sleep(2)

mainmenu = driver.find_element_by_class_name("sf-mainmenu")

print mainmenu

mainmenu.click()


# signup_item = driver.find_element_by_id("register")
#signup_item = driver.find_element_by_xpath(".//div//*[@id='register']")
# signup_item.click()

time.sleep(2)

# account_type = driver.find_element_by_id("accountType")
# account_type.click()
#
# type_business = driver.find_element_by_name("Business")
# type_business.click()

driver.quit()