#!/usr/bin/python3
"""
This python script lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
Usage : ./9-model_state_fetch_a.py <mysql username>
                                   <mysql password>
                                   <database name>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
