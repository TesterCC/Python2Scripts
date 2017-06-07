# coding:utf-8

import unittest
import requests

class JenkinsPost(unittest.TestCase):
	def setUp(self):
		self.build_job_url = 'http://192.168.2.141:8080/job/RFTestSetLaunchAppium/build'

	def test_build_job(self):
		r = requests.post(self.build_job_url, data={}, auth=('admin', 'globalroam123456'))
		print r.status_code
		# self.assertEqual(r.status_code, 201)  # can build - 201, cannot build - 500

if __name__ == '__main__':
	unittest.main()