#!/usr/bin/env python
#coding=utf-8

# 爬取糗事百科文章

from selenium import webdriver
class Qiubai:

    def __init__(self):
        #self.dr = webdriver.PhantomJS()
        self.dr = webdriver.Firefox()
        self.dr.get('http://www.qiushibaike.com/')

    def print_content(self):
        main_content = self.dr.find_element_by_id('content-left')

        i = 1
        for content in main_content.find_elements_by_class_name('content'):
            try:
                print(str(i) + ". " + content.text.encode("utf-8")) # .encode("utf-8") 转换乱码为正常中文
                print
                i = i + 1
            except UnicodeEncodeError:
                continue
        self.quit()

    def quit(self):
        self.dr.quit()


Qiubai().print_content()
