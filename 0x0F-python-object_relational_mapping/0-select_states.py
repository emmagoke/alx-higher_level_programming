#!/usr/bin/python3
"""
This python script all states from the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

user = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]  # Database name
db = MySQLdb.connect(host="localhost", port=3306, user=user,
                     passwd=password, db=db_name, charset="utf8")

cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC;")

query = cur.fetchall()
for row in query:
    print(row)
cur.close()
db.close()
