#!/usr/bin/python3
"""
This python script prints the first State object from the
database hbtn_0e_6_usa and If the table states is empty,
print Nothing followed by a new line.
Usage : ./8-model_state_fetch_first.py <mysql username>
                                       <mysql password>
                                       <database name>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).first()

    if query:
        print(f"{query.id}: {query.name}")
    else:
        print('Nothing')
    session.close()
