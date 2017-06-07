#coding:utf-8
'''
Created on 2016年2月29日

@author: PavilionLYX
'''
#xlutils.copy
from xlutils import copy
import xlrd

wkb_rd=xlrd.open_workbook('test.xls'); #默认相对路径为项目根目录下，建议填写绝对路径
wkb_cp=copy.copy(wkb_rd)

sheet=wkb_cp.get_sheet(0)
sheet.write(1,0,'yy')
sheet.write(1,1,'16')

wkb_cp.save('test_cp.xls')
