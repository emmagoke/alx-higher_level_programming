#!/usr/bin/python3
"""
This script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument.
Usage: ./1-filter_states.py <mysql username>
                            <mysql password>
                            <database name >
                            <state name searched>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=db_name)
    cur = db.cursor()
    query_str = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;" \
                .format(search)
    cur.execute(query_str)
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
