#!/usr/bin/env python
#coding=utf-8

'''
Testing Python -- P21-22
'''

import unittest
from calculate2 import Calculate

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    # def test_add_method_returns_correct_result(self):
    #     self.assertEqual("HelloWorld", self.calc.add("Hello", "World"))

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")

if __name__ == '__main__':
    unittest.main()