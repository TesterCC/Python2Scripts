# coding:utf-8
# !/usr/bin/env python

# Testing Python pdf P18-19

import unittest
from calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_return_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add_method_return_fault_result(self):
        self.assertEqual(4, self.calc.add(2, 3))


if __name__ == '__main__':
    unittest.main()
