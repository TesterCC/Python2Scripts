# coding: utf-8

import xlrd

file= 'testcases.xls'
data = xlrd.open_workbook(file)
table = data.sheet_by_name(u'TestCases')
sum_cell = 0

for i in range(table.nrows):
    for j in range(table.row_len(i)):
        sum_cell = sum_cell +1

print sum_cell


