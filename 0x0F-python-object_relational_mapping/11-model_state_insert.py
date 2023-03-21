#!/usr/bin/python3
"""
This python script adds the State object “Louisiana” to the
database hbtn_0e_6_usa
Usage : ./11-model_state_insert.py <mysql username>
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(f"{new_state.id}")
    session.close()
