#!/usr/bin/env python
#coding:utf-8

import os
# from HTMLTestRunner import HTMLTestRunner  # if create dir HTMLTestRunner and mv HTMLTestRunner.py in it.
import HTMLTestRunner     #  if put HTMLTestRunner.py in /Library/Python/2.7/site-packages directly
# directlyWindows平台：
# 将下载的文件放入...\Python27\Lib 目录下
# Linux平台：
# 下需要先确定 python 的安装目录，打开终端，输入 python 命令进入 python 交互模式，通过 sys.path 可以查看本机 python 文件
# 目录，以管理员身份将 HTMLTestRunner.py 文件考本到/usr/lib/python2.7/dist-packages/ 目录下
import unittest
import time
import logging

from appium import webdriver


'''
Pre-condition: Already login Pfingo app, launch appium client (--noset) without reinstall.
'''

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class elementA(unittest.TestCase):
    def test_callout(self):
        self.pacakage_name = 'com.globalroam.pfingo'
        self.launch_activity = '.ui.WelcomeActivity'
        desired_caps = {}
        desired_caps['deviceName'] = '87f3c408'  #adb devices查到的设备名 87f3c408
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['appPackage'] = self.pacakage_name  #被测App的包名
        desired_caps['appActivity'] = self.launch_activity #启动时的Activity
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

        el = driver.find_element_by_id('com.globalroam.pfingo:id/main_tab_button_1')
        el.click()
        time.sleep(3)

        # long press
        key0 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit00')
        key1 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit1')
        key2 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit2')
        key3 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit3')
        key4 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit4')
        key5 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit5')
        key6 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit6')
        key7 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit7')
        key8 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit8')
        key9 = driver.find_element_by_id('com.globalroam.pfingo:id/Digit9')

#         action1 = TouchAction(driver)
#         action1.long_press(key0,(720,1920),(720,1925), 4000)
        driver.swipe(720,1920,720,1920, 3000)

        key8.click()
        key6.click()
        key1.click()
        key3.click()
        key5.click()
        key5.click()
        key1.click()
        key8.click()
        key5.click()
        key6.click()
        key6.click()
        key4.click()
        key0.click()

        time.sleep(1)

        call = driver.find_element_by_id('com.globalroam.pfingo:id/call')
        call.click()

        time.sleep(1)

        callout_btn = driver.find_element_by_name("Call Out")
        callout_btn.click()

        time.sleep(2)

        speaker_btn = driver.find_element_by_id("com.globalroam.pfingo:id/speaker")
        speaker_btn.click()

        time.sleep(7)

        try:
            hangup_btn = driver.find_element_by_id("com.globalroam.pfingo:id/endBtn")
            hangup_btn.click()
        except Exception as e:
            logging.exception(e)
        finally:
            print("Run Testscript Error.")

        time.sleep(2)

        driver.quit()


if __name__ == '__main__':
    testunit=unittest.TestSuite()        #定义一个单元测试容器
    testunit.addTest(elementA("test_callout"))  #将测试用例加入到测试容器中
    filename="./testAppiumLog.html"        #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                                           stream=fp,
                                           title='Pfingo_Android_Callout_Test_Report',
                                           description='Report_Details')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)                 #自动进行测试
    # fp.close()                           #以防报告内容为空