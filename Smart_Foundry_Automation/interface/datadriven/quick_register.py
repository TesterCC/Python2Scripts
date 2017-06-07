#!/usr/bin/env python
# coding: utf-8
'''
learn from ceshibaixiaosheng python
'''

import xlrd

def getexcel(filepath="./",filename="testcases.xls"):
    '''
    Method to get Excel content
    :param filepath:
    :param filename:
    :return:
    '''
    file = filepath+filename
    print "File name: %s" % file
    data = xlrd.open_workbook(file)
    table = data.sheet_by_name(u'Test Accounts')
    nrows = table.nrows
    print "Total Rows: %s " % nrows

    item = range(3,nrows)   # 0,1,2 rows no need.
    print "Rows range: %s" % item

    print "========Basic Info Read========"
    for i in item:
        r = table.row_values(i)
        # print r[1],r[2].encode("utf-8")
        print r[1], r[2], r[3]     # r[0] -- No.column
    print "========Basic Info Get========"

#simple get method
# print (table.row_values(0))[0],(table.row_values(0))[1].encode("utf-8")
# print (table.row_values(1))[0],(table.row_values(1))[1].encode("utf-8")
# print (table.row_values(2))[0],(table.row_values(2))[1].encode("utf-8")
# print (table.row_values(3))[0],(table.row_values(3))[1].encode("utf-8")

if __name__ == '__main__':
    getresult = getexcel()