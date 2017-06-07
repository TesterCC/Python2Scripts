# coding: utf-8
import unittest
import requests
import json

# post /api/authuser
# http://gruc.gnum.com/static/swagger/swagger-ui/dist/index.html#!/%2Fapi%2Fauth_account_authenticate/post_api_authuser

class DefaultLoginTestCase(unittest.TestCase):

	def setUp(self):
		# if ENV['test_env'] == 'production'
		# 	self.domain = 'http://xxxx:3333'
		# else
		# 	self.domain = 'http://localhost:12306'
		self.domain = 'http://gruc.gnum.com'
		self.json_headers = {'content-type': 'application/json'}
		print 'before each test'

	def tearDown(self):
		print 'after each test'

	def test_login_post(self):
		print 'test login -- POST'
		json_data = json.dumps({'domain': 'uc', 'mobile': '8613551856640', 'password': '123456'})

		r = requests.post(self.url('/api/authuser'), data=json_data, headers=self.json_headers)
		result = r.json()

		self.assertEqual(r.status_code, 200)
		self.assertEqual(result['username'], 'yanxi')
		self.assertEqual(result['id'], 'subusr1468983481000')


# set api rul
	def url(self, path):
		return self.domain + path


if __name__ == '__main__':
	unittest.main()