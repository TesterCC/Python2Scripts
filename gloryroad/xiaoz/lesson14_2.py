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

#先定义一条SQL语句
sql="insert into msg(title,name,content) values(%s,%s,%s)"

#valuess=[('test05','zz05','test content05'),('test06','zz06','test content06')]

#插入多条数据
cur.executemany(sql,[('test05','zz05','test content05'),('test06','zz06','test content06')])

conn.commit()  #不用这句数据不会真正添加到database中
