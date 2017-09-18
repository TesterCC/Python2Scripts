#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/18 20:58'


'''
To test selenium lib installed.

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247483673&idx=1&sn=1b6992463869a5249224f015ee7e5c32&scene=19#wechat_redirect
'''

from selenium import webdriver
from time import sleep


if __name__ == '__main__':
    driver = webdriver.Chrome()    # 初始化一个webdriver实例
    driver.get("http://www.baidu.com")     # visite baidu.com
    sleep(5)       # wait 5s
    driver.close()     # close browser
