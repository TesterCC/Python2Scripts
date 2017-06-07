# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) 2014 by Administrator.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
# 1.在testbean的包里新建三个类,分别是testcasecounter, testcaselistcounter, testcasesuitecounter, 分别用于统计用例结果, 统计接口测试列表结果, 测试套件结果.
#
# 2.在testcasecounter中实现 “set_start_time”, “get_start_time”, “set_end_time”, “get_end_time”, “get_duration_time”, “set_test_case”, “get_test_case”, “set_result_object”, “get_result_object”等方法用于设置\获取testcase数据结构及运行时的开始\结束\运行结果等方法.
#
# 3.在testcaselistcounter中实现” set_api_http_url”,” get_api_http_url”,” set_api_http_method”,” get_api_http_method”,” set_api_desc”,” get_api_desc”,” get_pass_count”,” get_fail_count”,” get_error_count”,” get_skip_count”,” set_start_time”,” get_start_time”,” set_end_time”,” get_end_time”,” get_duration_time”,” append_test_case_counter”,” get_test_case_counter_list”,” get_test_case_counter_length”,” get_result_object”等方法,用于设置API测试列表的信息,运行时的成功失败结果等


class TestCaseCounter(object):
    def __init__(self):
        self._start_time = None
        self._end_time = None
        self._duration_time = None
        self._result_object = {}
        self._test_case = None
        self._error_count = 0
        self._pass_count = 0
        self._fail_count = 0

    def set_start_time(self,start_time):
        self._start_time = start_time

    def get_start_time(self):
        return self._start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def get_end_time(self):
        return self._end_time

    def get_duration_time(self):
        self._duration_time = self._end_time - self._start_time
        return self._duration_time

    def set_result_object(self, result, running_message):
        self._result_object = {"result": result, "msg": running_message}

    def get_result_object(self):
        return self._result_object

    def get_result_object_with_key(self, key):
        if key in self._result_object.keys():
            return self._result_object[key]
        else:
            return ""

    def set_test_case(self, test_case):
        self._test_case = test_case

    def get_test_case(self):
        return self._test_case







