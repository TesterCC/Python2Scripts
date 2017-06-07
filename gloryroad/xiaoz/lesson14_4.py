#coding:utf-8
'''
Created on 2016年3月16日

@author: PavilionLYX
'''

import MySQLdb


conn=MySQLdb.connect(host="127.0.0.1",user="root",
                     passwd="yanxi76543210",
                     db="test",port=3306,charset="utf8")

cur=conn.cursor()

print cur.execute("select * from user");

#打印表中全部数据,要先execute，否则会报错
print cur.fetchall()

print cur.fetchall()

#其实位置为0
cur.scroll(0,mode='absolute')
print cur.fetchmany(1)  #只取一条数据

cur.scroll(0,mode='relative')
print cur.fetchmany(1) 

cur.scroll(0,mode='absolute')
row = cur.fetchone()
while row:
    print row[2]  #gender
    row = cur.fetchone()

#关闭游标
cur.close()

#关闭数据库连接
conn.close()