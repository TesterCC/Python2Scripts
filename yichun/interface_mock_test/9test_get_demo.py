# coding:utf-8
import unittest
import json
import requests

class JenkinsGetTestCase(unittest.TestCase):

	def setUp(self):
		self.r = requests.get('http://192.168.2.141:8080/api/json?tree=jobs[name]')

	def test_get_all_job_names(self):
		result = self.r.text  #已字符串打印返回的json
		json_result = json.loads(result)  # json反序列化->python dict
		print json_result

		#Write Assertion
		self.assertEqual(json_result['jobs'][0]['name'],'CheckNodejsVersion'); #first project name
		self.assertEqual(json_result['jobs'][-1]['name'],'WebBudgetRoamDemo'); #last project name

	def test_get_all_job_names_simple_way(self):
		json_result = self.r.json()
		#Write Assertion
		self.assertEqual(json_result['jobs'][0]['name'],'CheckNodejsVersion'); #first project name
		self.assertEqual(json_result['jobs'][-1]['name'],'WebBudgetRoamDemo'); #last project name


if __name__ == '__main__':
	unittest.main()