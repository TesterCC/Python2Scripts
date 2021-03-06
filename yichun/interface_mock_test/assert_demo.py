# coding: utf-8
import unittest

def div(a,b):
	return a/b

class TestDiv(unittest.TestCase):

	def test_1_div_1(self):
		print '1 div 1'
		self.assertEqual(div(1,1),1/1)

	def test_3_div_4(self):
		print '3 div 4'
		self.assertEqual(div(3,4),3/4)

	def test_3_div_0(self):
		print '3 div 0'
		self.assertRaises(ZeroDivisionError,div,3,0)



class MyFirstTestCase(unittest.TestCase):
	def setUp(self):
		print 'run before each test'

	def tearDown(self):
		print 'run after each test'

	def test_sample(self):
		print 'test sample'

if __name__=='__main__':
	unittest.main()