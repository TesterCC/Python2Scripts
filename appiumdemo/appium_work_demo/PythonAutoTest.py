#coding:utf-8  pass windows and mac  pass on xiaomi2s(root) but failed in Samsung note4 
import os
import time
from appium import webdriver   #need install Appium-Python-Client-0.16.tar.gz

desired_caps = {}
desired_caps['deviceName'] = '434aab08'  #adb devices查到的name
#xiaomi2s   434aab08
#samsungS5   e90bb2d1
#HTC one m8  HC44WWM01499
#Samsung Note3 32041a4eb592c0bf
#Samsung Note4 84b8c68c
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.1'      
desired_caps['appPackage'] = 'com.android.calculator2'  #被测App的包名
desired_caps['appActivity'] = '.Calculator' #启动时的Activity
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
CButton = driver.find_element_by_id('com.android.calculator2:id/digit8')
CButton.click() 
CButton1 = driver.find_element_by_id('com.android.calculator2:id/digit2')
CButton1.click() 
 
time.sleep(3)       
driver.quit()