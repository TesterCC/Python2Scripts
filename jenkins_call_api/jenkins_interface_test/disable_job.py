# coding:utf-8

import unittest
import requests

class JenkinsPost(unittest.TestCase):
	def setUp(self):
		self.disable_job_url = 'http://192.168.2.141:8080/job/RFTestSetLaunchAppium/disable'
		self.job_url = 'http://192.168.2.141:8080/job/RFTestSetLaunchAppium/api/json'

	def test_disable_job(self):
		status = self.get_job_status()
		# self.assertTrue(status)
		print status

		r = requests.post(self.disable_job_url, data={}, auth=('admin', 'globalroam123456'))
		# print r.status_code
		self.assertEqual(r.status_code, 200)

		status = self.get_job_status()
		# self.assertFalse(status)

# get job status
	def get_job_status(self):
		job_info = requests.get(self.job_url, auth=('admin', 'globalroam123456')).json()
		return job_info['buildable']
		return job_info

if __name__ == '__main__':
	unittest.main()