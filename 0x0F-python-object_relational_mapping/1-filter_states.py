#!/usr/bin/python3
"""
This script lists lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    query = cur.fetchall()
    for row in query:
        if row[1][0] != 'n':
            print(row)
    cur.close()
    db.close()
