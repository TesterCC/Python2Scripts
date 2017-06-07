#-*- coding:utf-8 -*-#
'''
Created on 2015年11月10日
公开课第三讲 流程控制1  loop sentence
求1到100的和
@author: PavilionLYX
'''

import time

for i in range(10):
    print i
    if i == 1:
        pass  #代码桩
    if i == 2:
        print "===222222==="
        continue
    if i == 5:
        break
    print "*"*15
    
    time.sleep(1)
else:
    print "Bye"
    
for i in range(3):
    print 3
