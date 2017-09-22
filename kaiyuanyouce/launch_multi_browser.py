#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 21:54'


'''
Python多线程Selenium跨浏览器测试
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247483739&idx=1&sn=f0a2d7251fd7ea095473dec7a842527a&scene=19#wechat_redirect
'''

import sys
from time import sleep
from threading import Thread

from selenium import webdriver

reload(sys)
sys.setdefaultencoding("utf-8")


def test_baidu_search(browser, url):
    driver = None

    # 你可以自定义这里，添加更多浏览器支持进来
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        print(u"输入不合法，请确认后再尝试")

    if driver == None:
        print(u"driver为空，退出运行")
        exit()

    print u"开始[case_0001]百度搜索"
    driver.get(url)

    print u"清除搜索中数据，输入搜索关键词"
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(u"全栈测试")

    print u"单击 百度一下 按钮 开始搜索"
    driver.find_element_by_id("su").click()
    sleep(3)

    print u"关闭浏览器，退出webdriver"
    driver.quit()


if __name__ == '__main__':
# 浏览器和首页url,可以参数化这个部分
     data = {
        "chrome": "http://www.baidu.com",
        "firefox": "http://www.baidu.com"    # firefox因为和Selenium2的兼容性问题，可以启动但无法输入
        # "ie": "http://www.baidu.com",
    }

# 构建线程
threads = []
for b, url in data.items():
    t = Thread(target=test_baidu_search, args=(b, url))
    threads.append(t)

# 启动所有线程
for thr in threads:
    thr.start()

