#!/usr/bin/env python
# coding:utf-8
from time import sleep

from selenium import webdriver
import public

username = "yanxi";
password = "yanxi76543210"
baseurl = "http://intranet.gnum.com/wp-login.php"

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(public.baseurl)
public.login(driver)

sleep(2000)

# click,edit etc.

public.logout(driver)