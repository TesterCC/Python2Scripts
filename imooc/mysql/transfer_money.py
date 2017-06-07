#!/usr/bin/python
# coding:utf-8

# run with parameters >>>> Edit configuration -- script parameters -- apply and run

import sys

import MySQLdb


class TransferMoney(object):
    def __init__(self,conn):
        self.conn = conn

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            cursor = self.conn.cursor()
            sql = "select * from account where acctid=%s" % acctid
            cursor.execute(sql)
            print "check_acct_available: " + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("Account %s is not exist" % acctid)
        finally:
            cursor.close()


    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            cursor = self.conn.cursor()
            sql = "select * from account where acctid=%s and money>%s " % (acctid, money)
            cursor.execute(sql)
            print "check_enough_monkey: " + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("Account %s has no enough money." % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            cursor = self.conn.cursor()
            sql = "update account set money=money-%s where acctid=%s" % (money,acctid)
            cursor.execute(sql)
            print "reduce_monkey: " + sql
            if cursor.rowcount != 1:
                raise Exception("Account %s reduce money failed." % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            cursor = self.conn.cursor()
            sql = "update account set money=money+%s where acctid=%s" % (money,acctid)
            cursor.execute(sql)
            print "add_monkey: " + sql
            if cursor.rowcount != 1:
                raise Exception("Account %s add money failed." % acctid)
        finally:
            cursor.close()

if __name__ == "__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    conn = MySQLdb.Connect(host='127.0.0.1', user='root', passwd='yanxi76543210', port=3306, db='imooc')
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print "Find error: " + str(e)
    finally:
        conn.close()
