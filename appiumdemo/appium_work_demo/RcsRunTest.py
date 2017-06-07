#coding:utf-8 pass windows and mac
import os
import time
from appium import webdriver   #need install Appium-Python-Client-0.16.tar.gz

desired_caps = {}
desired_caps['deviceName'] = '93e2da8b'  #adb devices查到的name
#xiaomi2s   434aab08
#samsungS5   e90bb2d1
#HTC one m8  HC44WWM01499
#Samsung Note3 32041a4eb592c0bf
#Samsung Note4 84b8c68c
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.1'      
desired_caps['appPackage'] = 'com.starhub.messageplus'  #被测App的包名
desired_caps['appActivity'] = '.login.LoginSlapshActivity' #启动时的Activity
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3) 
      
username = driver.find_element_by_id('com.starhub.messageplus:id/enter_number')
username.click()
username.send_keys('98805408')
time.sleep(2)

                
#driver.quit()