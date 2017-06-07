# coding: utf-8
# 思路，代码应该还有问题
# http://www.chuanyuebook.com/study_question?courseid=3&day=7&openid=oybJvwqmQsdB2T-P7DjAwTsvNNIU&showanswer=1

import xlrd

file= 'testcases.xls'
data = xlrd.open_workbook(file)
test_case_sheet = data.sheet_by_name(u'TestCases')


def TestCaseInfo():
    test_case_length=28
    for i in range(5, test_case_length):
        test_case_id = int(test_case_sheet.cell(i,0).value)
        test_case_is_run = test_case_sheet.cell(i,1).value
        test_case_http_body = test_case_sheet.cell(i,2).value
        test_case_assert_pattern = test_case_sheet.cell(i,3).value
        test_case_assert_value = test_case_sheet.cell(i,4).value
        test_case_desc = test_case_sheet.cell(i,5).value

        print test_case_id,test_case_is_run,test_case_http_body,test_case_assert_pattern,test_case_assert_value.encode("utf-8"),test_case_desc.encode("utf-8")

        # test_case_info = test_case_id,test_case_is_run,test_case_http_body,test_case_assert_pattern,test_case_assert_value.encode("utf-8"),test_case_desc.encode("utf-8")

        # test_case_list = []
        # test_case_list = test_case_list.append(test_case_info)
        # # test_case_list.append_test_case(test_case_info)

        # print test_case_info

if __name__ == "__main__":
    TestCaseInfo()


