# coding: utf-8

import xlrd

file= 'testcases.xls'
data = xlrd.open_workbook(file)
table = data.sheet_by_name(u'TestCases')


item = [0,1,2,3]

for i in item:
    r = table.row_values(i)
    print r[0],r[1].encode("utf-8")
print "========Basic Info========"

#simple get method
# print (table.row_values(0))[0],(table.row_values(0))[1].encode("utf-8")
# print (table.row_values(1))[0],(table.row_values(1))[1].encode("utf-8")
# print (table.row_values(2))[0],(table.row_values(2))[1].encode("utf-8")
# print (table.row_values(3))[0],(table.row_values(3))[1].encode("utf-8")
