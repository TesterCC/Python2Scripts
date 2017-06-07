#!/usr/bin/env python
#coding=utf-8

# Testing Python pdf P22

import unittest
from calculate2 import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_return_correct_result(self):
        self.assertEqual("HelloWorld", self.calc.add("Hello", "World"))


if __name__ == '__main__':
    unittest.main()
