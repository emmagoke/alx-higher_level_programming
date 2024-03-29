#!/usr/bin/python3
"""
This python script deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
Usage : ./13-model_state_delete_a.py <mysql username>
                                     <mysql password>
                                     <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
        session.delete(state)
    session.commit()
    session.close()
