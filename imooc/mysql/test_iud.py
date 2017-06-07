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

sql_insert = "insert into user(userid, username) values(11, 'name11')"

sql_update = "update user set username='name91' where userid=9"

sql_delete = "delete from user where userid<3"
# sql_delete = "delete from user where userd<3"

try:
    cursor.execute(sql_insert)
    print cursor.rowcount    # 造成了多少行的影响

    cursor.execute(sql_update)
    print cursor.rowcount

    cursor.execute(sql_delete)
    print cursor.rowcount

    conn.commit()   # 默认mysqldb关闭，需要提交这句执行才能生效

except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()