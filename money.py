#coding:utf8
import sys
import MySQLdb

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn
    def transfer(self, sid, tid, money):
        try:
            self.check_acct_available(sid)
            self.check_acct_available(tid)
            self.has_enough_money(sid, money)
            self.reduce_money(sid, money)
            self.add_money(tid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, account_id):
        try:
            cursor = self.conn.cursor()
            sql = "select * from account where id = '%s'" % account_id
            print "check account available:" + sql
            if cursor.rowcount == 0:
                raise Exception("Account not exist" + account_id)
        finally:
            cursor.close()

    def has_enough_money(self, account_id, money):
        try:
            cursor = self.conn.cursor()
            sql = "select * from account where id = '%s' and money >= %s" % (account_id, money)
            cursor.execute(sql)
            print "check enough money:" + sql
            if cursor.rowcount == 0:
                raise Exception("帐户%s没有足够的钱" % account_id)
        finally:
            cursor.close()

    def reduce_money(self, account_id, money):
        try:
            cursor = self.conn.cursor()
            sql = "update account set money = money - %s WHERE id = %s" % (money, account_id)
            cursor.execute(sql)
            print "check enough money:" + sql
            if cursor.rowcount == 0:
                raise Exception("Reduce Money Fail")
        finally:
            cursor.close()

    def add_money(self, account_id, money):
        try:
            cursor = self.conn.cursor()
            sql = "update account set money = money + %s WHERE id = %s" % (money, account_id)
            cursor.execute(sql)
            print "add_money:" + sql
            if cursor.rowcount == 0:
                raise Exception("Add Money Fail")
        finally:
            cursor.close()

if __name__ == "__main__":
    print sys.argv
    sid = sys.argv[1]
    tid = sys.argv[2]
    money = sys.argv[3]

    conn = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="111111",
        db="test",
        charset="utf8"
    )
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(sid, tid, money)
    except Exception as e:
        print "出现问题：" + str(e)
    finally:
        conn.close()