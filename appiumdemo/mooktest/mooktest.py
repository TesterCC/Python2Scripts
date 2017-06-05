#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = '416124ea'
desired_caps['appPackage'] = 'com.mook.mook'
desired_caps['appActivity'] = '.LoginActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("email").send_keys("mooktest")
driver.find_element_by_id("password").send_keys("mooktest")
driver.find_element_by_id("email_sign_in_button").click()

try:
    if driver.find_element_by_id("email_sign_in_button").is_displayed():
        print "fail"
except Exception, e:
        print e
        print "pass"

driver.quit()

time.sleep(5)
