#!/usr/bin/env python
#coding=utf-8

import unittest
import requests

class GetUI(unittest.TestCase):
    '''
    但是GRUC的API早就down了，留作纪念
    '''
    def setUp(self):
        self.r = requests.get('http://gruc.gnum.com/ui/xxxx')

	def test_get_all_job_names(self):
		result = self.r.text  #以字符串打印返回的内容
		print result

if __name__ == '__main__':
	unittest.main()