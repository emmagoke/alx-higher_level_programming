#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
Usage: ./5-filter__states.py <mysql username>
                             <mysql password>
                             <database name>
                             <state name>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    s_name = sys.argv[4].split(' ')[0]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states JOIN cities ON "
                "states.id=cities.state_id WHERE states.name LIKE BINARY "
                "'{}'".format(s_name))
    out = []
    for row in cur.fetchall():
        out.append(row[0])
    print(", ".join(out))
    cur.close()
    db.close()
