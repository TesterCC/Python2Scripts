#!/usr/bin/python
# coding:utf-8

class HtmlReprotGen(object):
    def __init__(self):
        self._summary_table = []
        self._details_table = []
        self._test_case_details_content = ""
        self._report = []

    def generate_summary_table(self,summary_table):
        self._summary_table = summary_table


