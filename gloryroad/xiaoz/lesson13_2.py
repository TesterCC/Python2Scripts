#coding:utf-8
'''
Created on 2016年2月29日

@author: PavilionLYX
'''
#Failed
import xlwt
wkb=xlwt.Workbook('test.xls'); #默认相对路径为项目根目录下，建议填写绝对路径
# wkb=xlwt.Workbook('E:\\workspace\\PythonDemo\\gloryroadpythondemo\\test.xls')  #默认相对路径为项目根目录下，建议填写绝对路径
sheet=wkb.add_sheet('Sheet4',cell_overwrite_ok=True) 
# sheet=sheet.decode('utf_16_le')
sheet.write(0,0,'zz')
wkb.save('text1.xls') #只支持保存为xls格式

