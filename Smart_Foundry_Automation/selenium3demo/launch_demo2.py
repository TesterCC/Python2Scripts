#!/usr/bin/env python
# coding:utf-8

import unittest
from selenium import webdriver


chrome_path = "/Users/TesterCC/Development/webdriver/chromedriver"

firefox_path = "/Users/TesterCC/Development/webdriver/geckodriver"

safari_path = "/usr/bin/safaridriver"

# selenium_server_jar = "/Users/TesterCC/Downloads/seleni-server-standalone-3.0.1.jar"


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chrome_path)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://www.gnum.com/')
        self.assertIn('GNum', self.browser.title)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
