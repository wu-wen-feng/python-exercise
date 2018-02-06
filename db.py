import MySQLdb
conn = MySQLdb.Connect(
    host="192.168.182.3",
    port=3306,
    user="root",
    passwd="111111",
    db="test",
    charset="utf8"
)
conn.autocommit(False)
cursor = conn.cursor()
print conn
print  cursor
# select
cursor.execute("select * from test")
print cursor.rowcount
print cursor.fetchone()
print cursor.fetchmany(3)
ret = cursor.fetchall()
for row in ret:
    print "t_id=%s, t_name=%s" % row
try:
    cursor.execute("insert into test(name) VALUES('111')")
    cursor.execute("insert into test(name) VALUES('222')")
    cursor.execute("insert into test(name) VALUES('333')")
    conn.commit()
except Exception as e:
    print e
    #conn.rollback()
conn.close()
cursor.close()