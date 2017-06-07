#-*- coding:utf-8 -*-#
'''
Created on 2015年11月10日
公开课第三讲 流程控制1
@author: PavilionLYX
'''

score=raw_input("Please input score:")
score=int(score)

if score > 85:
    print "good"
elif 60 < score <= 85:
    print "pass"
else:
    print "failed"