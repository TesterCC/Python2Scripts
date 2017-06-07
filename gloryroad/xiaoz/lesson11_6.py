#coding:utf-8
'''
Created on 2016年2月22日

@author: PavilionLYX
'''
#time
import time
from twisted.python.runtime import seconds

print time.time() #return timestamp

a=time.localtime()
print a
#tm_wday=0-->refer to Monday, 
#tm_yday=53-->refer the 53th day of this year
#tm_isdst=0-->是否是夏令时，0表示false，不是

timestamp=1456122848.74
b=time.localtime(timestamp)
print b

print time.mktime(a)  #return timestamp
print time.mktime(b)

#格式化返回时间
print time.asctime()
print time.asctime(b)

print time.ctime()
print time.ctime(timestamp)

print "==================================="
print time.strftime('%Y-%m-%d %H:%M:%S')
print time.strftime('%y-%m-%d %H:%M:%S')

#返回一小时前的时间元组
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()-3600))
#1 hour = 3600 s

print time.strptime('2016-02-22 18:18:36','%Y-%m-%d %H:%M:%S')

time.sleep(2)  #Unit is secord,wait for X seconds