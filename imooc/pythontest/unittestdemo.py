# coding:utf-8
# !/usr/bin/env python

import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        '''before execute test'''
        print "setup"

    def testCase(self):
        '''actual testcase'''
        print "test case"

    def tearDown(self):
        '''after test, release resource'''
        print "teardown"

if __name__ == '__main__':
    unittest.main()