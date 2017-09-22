#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 17:17'


'''
Python Selenium设计模式-POM
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247483736&idx=1&sn=e282ed9c14888ea574a067d442fcb27e&scene=19#wechat_redirect
'''

# 主入口程序代码如下

import unittest
import sys

from common import HTMLTestRunner
from testcase.testSearchPage import TestSearchPage
from testcase.testSearchPageUseData import TestSearchPageUseData

reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # test1
    # testunit.addTest(TestSearchPage('testSearch'))

    # test2
    testunit.addTest(TestSearchPageUseData('testSearch'))   # can't find xls file

    # 定义报告输出路径
    htmlPath = u"page_demo_Report.html"
    fp = file(htmlPath, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"百度测试",
                                           description=u"测试用例结果")

    runner.run(testunit)

    fp.close()
