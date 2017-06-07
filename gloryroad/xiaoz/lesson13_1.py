#coding:utf-8
'''
Created on 2016年2月29日

@author: PavilionLYX
'''

import xlrd
wkb=xlrd.open_workbook('test.xls'); #默认相对路径为项目根目录下，建议填写绝对路径
# wkb=xlrd.open_workbook('E:\\workspace\\PythonDemo\\gloryroadpythondemo\\test.xls'); #默认相对路径为项目根目录下，建议填写绝对路径
print wkb.sheet_names();#get all sheets name
print wkb.sheets()[0];
print wkb.sheet_by_index(0);
print wkb.sheet_by_name('Sheet1');

sheet=wkb.sheets()[0]
print sheet.nrows  #行数
print sheet.ncols  #列数
print sheet.row_values(0)
print sheet.col_values(0)
#第一行第二列,first row-second columns
print "-----------------------------"
print sheet.cell(0,1).value
print sheet.cell_value(0,1)
print sheet.row(0)[1].value
print sheet.col(1)[0].value

print wkb.encoding
