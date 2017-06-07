#-*- coding:utf-8 -*-#
'''
测试一下
@author: PavilionLYX
'''

from selenium import webdriver
# import time  #time.sleep(2);
from time import sleep

dr = webdriver.Chrome()
dr.maximize_window() #maximum browser
# dr = webdriver.Firefox()
url = 'https://www.baidu.com/'  # http://www.tokuapp.com/


print "now access %s" %(url)
dr.get(url)

print "now input keywords"
dr.find_element_by_id("kw").send_keys("selenium")
sleep(2);

print "now click search button"
dr.find_element_by_id("su").click()
sleep(2);
dr.quit()
