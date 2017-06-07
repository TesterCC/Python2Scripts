# coding: utf-8
import unittest
import requests
import json

# POST /api/op/otp_login
# http://gruc.gnum.com/static/swagger/swagger-ui/dist/index.html#/

class RequestOTPLoginTestCase(unittest.TestCase):

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
		print 'Request OTP login -- POST'
		json_data = json.dumps({'domain': 'uc', 'mobile': '8613551856640'})

		r = requests.post(self.url('/api/op/otp_login'), data=json_data, headers=self.json_headers)
		result = r.json()

		self.assertEqual(r.status_code, 200)
		self.assertEqual(result['msg'], 'sms sended')


# set api rul
	def url(self, path):
		return self.domain + path


if __name__ == '__main__':
	unittest.main()