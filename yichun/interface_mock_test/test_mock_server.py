#!/usr/bin/env python
#coding=utf-8


import unittest
import requests
import json


'''
乙醇接口测试教程代码
'''


class InterfaceTestCase(unittest.TestCase):

	def setUp(self):
		self.domain = 'http://localhost:12306'
		self.json_headers = {'content-type': 'application/json'}

	def tearDown(self):
		print 'after each test'

	def test_get_all_posts(self):
		print 'test get all posts'
		results = requests.get(self.url('/posts')).json()

		self.assertEqual(len(results), 3)

		self.assertEqual(results[0]['title'], 'first post')
		self.assertEqual(results[0]['url'], '/posts/1')

		self.assertEqual(results[-1]['title'], 'third post - how to test interface')
		self.assertEqual(results[-1]['url'], '/posts/3')

	def test_get_first_post(self):
		print 'test get first post'
		result = requests.get(self.url('/posts/1')).json()

		self.assertEqual(result['title'], 'first post')
		self.assertEqual(result['content'], 'It\'s my first post')

	def test_create_post(self):
		json_data = json.dumps({'title': 'new post', 'content': 'new post'})
		r = requests.post(self.url('/posts'), data=json_data, headers=self.json_headers)
		result = r.json()

		self.assertEqual(r.status_code, 200)
		self.assertEqual(result['success'], 'true')


	def test_edit_post(self):
		json_data = json.dumps({'title': 'new post', 'content': 'new post'})
		r = requests.put(self.url('/posts/1'), data=json_data, headers=self.json_headers)
		result = r.json()

		self.assertEqual(r.status_code, 200)
		self.assertEqual(result['success'], 'true')

	def test_delete_post(self):
		r = requests.delete(self.url('/posts/2'))
		result = r.json()

		self.assertEqual(r.status_code, 200)
		self.assertEqual(result['success'], 'true')


	def url(self, path):
		return self.domain + path



if __name__ == '__main__':
	unittest.main()
