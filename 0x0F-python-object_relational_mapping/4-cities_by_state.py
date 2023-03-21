#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
Usage: .4-cities_by__states.py <mysql username>
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM states JOIN"
                " cities ON states.id=cities.state_id ORDER BY cities.id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
