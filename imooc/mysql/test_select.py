#!/usr/bin/python
# coding:utf-8
import MySQLdb

conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='yanxi76543210',
    db='imooc',
    charset='utf8'
)

cursor = conn.cursor()

sql = "select * from user"

cursor.execute(sql)

rs = cursor.fetchall()

for row in rs:
    print "userid=%s, username=%s" % row
    # print "%s--%s" % row
    # print row

cursor.close()
conn.close()