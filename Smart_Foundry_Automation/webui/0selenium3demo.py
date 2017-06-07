#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test Selenium3 simple demo
Visit SmartFoundry Homepage
Complex structure may cause loacte Element report error.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

STR = 'SmartFoundry'

# browser = webdriver.Firefox()


browser = webdriver.Chrome()

browser.get('https://developer.smartfoundry.io')

print "Web page title ==> %s " % browser.title

assert STR in browser.title

# str = ("百度一下")
# assert str in browser.title


browser.quit()