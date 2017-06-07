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

#插入单条数据
cur.execute("insert into msg (title,name,content) values ('python','zz','test mysql insert')")
conn.commit()  #不用这句数据不会真正添加到database中
