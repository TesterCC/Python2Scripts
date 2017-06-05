# coding:utf-8
# !/usr/bin/env python

import unittest
import ddt

@ddt.ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print "setup"

    @ddt.data(["testdata1","expected_result1"],
              ["testdata2","expected_result2"],
              ["testdata3","expected_result3"])

    @ddt.unpack
    def testCase(self,testdata,expected_result):
        '''real testcases'''
        print "execute testcase"
        print testdata
        print expected_result

    def tearDown(self):
        print "teardown"


if __name__ == '__main__':
    unittest.main()