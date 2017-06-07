#coding: utf-8
import unittest
import requests

class InterfaceTestCase(unittest.TestCase):

	def setUp(self):
		# if ENV['test_env'] == 'production'
		# 	self.domain = 'http://xxxx:3333'
		# else
		# 	self.domain = 'http://localhost:12306'

		self.domain = 'http://localhost:12306'
		print 'before each test'

	def tearDown(self):
		print 'after each test'

	def test_get_all_posts(self):
		print 'test get all posts'
		results = requests.get(self.url('/posts')).json() #transfered to dict
		# print results.text

		#Assertion
		self.assertEqual(len(results),3)

		self.assertEqual(results[0]['title'],'first post')
		self.assertEqual(results[0]['url'],'/posts/1')

		self.assertEqual(results[-1]['title'],'third post - how to test interface')
		self.assertEqual(results[-1]['url'],'/posts/3')

	def test_get_first_post(self):
		print 'test get first post'
		result = requests.get(self.url('/posts/1')).json() #transfer to dict

		self.assertEqual(result['title'],'first post')
		self.assertEqual(result['content'],'It\'s my first post')

	def url(self,path):
		return self.domain + path


if __name__ == '__main__':
	unittest.main()