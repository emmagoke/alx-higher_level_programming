#!/usr/bin/python3
"""
This python file lists all State objects from the database hbtn_0e_6_usa
Usage : ./7-model_state_fetch_all.py <mysql username>
                                     <mysql password>
                                     <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           password, db_name), pool_pre_ping=True)
    # Configure the session class
    Session = sessionmaker(bind=engine)

    # extract a session
    session = Session()

    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
