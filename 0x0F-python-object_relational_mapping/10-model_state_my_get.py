#!/usr/bin/python3
"""
This python script prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Usage : ./10-model_state_my_get.py <mysql username>
                                   <mysql password>
                                   <database name>
                                   <state name to search>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    s_name = sys.argv[4].split(' ')[0]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == s_name).first()

    if query:
        print(f"{query.id}")
    else:
        print("Not found")
    session.close()
