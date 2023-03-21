#!/usr/bin/python3
"""
This script  takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the
argument. But this is safe from MySQL injections!
Usage: ./3-my_safe_filter_states.py <mysql username>
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
    search = sys.argv[4].split(' ')[0]

    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY "
                "'{}' ORDER BY id ASC;".format(search))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
