#coding:utf-8
'''
Created on 2016年3月16日

@author: PavilionLYX
'''

import MySQLdb
import random

conn=MySQLdb.connect(host="127.0.0.1",user="root",
                     passwd="yanxi76543210",
                     db="test",port=3306,charset="utf8")

cur=conn.cursor()

#利用for循环插入数据
#已创建新表user
sql="insert into user (name,gender) values"


for i in range(100):
    sql+=" ('user"+str(i)+"',"+str(random.randint(0,1))+"),"
    #最后是没有逗号的，需要处理下

sql=sql[:-1]
print sql

#insert data
cur.execute(sql)

conn.commit()  #不用这句数据不会真正添加到database中
