#coding:utf-8
import os
import HTMLTestRunner  #for HTMLReport  code in the end
import unittest
import time

from selenium import webdriver
 
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
 
class elementA(unittest.TestCase): 
    def test_(self):   
        desired_caps = {}
        desired_caps['deviceName'] = '93e2da8b'  #adb devices查到的设备名
        #xiaomi2s   434aab08
        #samsungS5   e90bb2d1
        #HTC one m8  HC44WWM01499
        #Samsung Note3 32041a4eb592c0bf
        #Samsung Note4 84b8c68c
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'      
        desired_caps['appPackage'] = 'com.starhub.messageplus'  #被测App的包名
        #com.starhub.messageplus
        desired_caps['appActivity'] = 'com.starhub.messageplus.login.LoginSlapshActivity' #启动时的Activity
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
        username = driver.find_element_by_id('com.starhub.messageplus:id/enter_number')
        username.click()
        username.send_keys('98805407')
        time.sleep(3)        
                 
        driver.quit()
#for HTML report     
if __name__ == '__main__':
    testunit=unittest.TestSuite()        #定义一个单元测试容器
    testunit.addTest(elementA("test_"))  #将测试用例加入到测试容器中    
    filename="C:/Users/PavilionLYX/Desktop/myAppiumLog.html"        #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)                 #自动进行测试