#coding: utf-8
import unittest
import requests
import json

class InterfaceTestCase(unittest.TestCase):

	def setUp(self):
		# if ENV['test_env'] == 'production'
		# 	self.domain = 'http://xxxx:3333'
		# else
		# 	self.domain = 'http://localhost:12306'
		self.domain = 'http://localhost:12306'
		self.json_headers = {'content-type': 'application/json'}
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

	def test_create_post(self):
		print 'test POST'
		json_data = json.dumps({'title': 'new post', 'content': 'new post'})
		r = requests.post(self.url('/posts'), data=json_data, headers=self.json_headers)
		result = r.json()

		self.assertEqual(r.status_code, 200)
		self.assertEqual(result['success'], 'true')

	def test_edit_post(self):
		print 'test edit'
		json_data = json.dumps({'title': 'new post', 'content': 'new post'})
		r = requests.put(self.url('/posts/1'), data=json_data, headers=self.json_headers)
		result = r.json()

		self.assertEqual(r.status_code, 200)
		self.assertEqual(result['success'], 'true')

	def test_delete_post(self):
		print 'test delete'
		json_data = json.dumps({'title': 'new post', 'content': 'new post'})
		r = requests.delete(self.url('/posts/2'))
		result = r.json()

		self.assertEqual(r.status_code, 200)
		self.assertEqual(result['success'], 'true')



#NameError: name 'self' is not defined
	def url(self,path):
		return self.domain + path


if __name__ == '__main__':
	unittest.main()