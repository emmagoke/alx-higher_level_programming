#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
Usage : ./100-relationship_states_cities.py <mysql username>
                                            <mysql password>
                                            <database name>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    city = City(name="San Francisco")
    state = State(name="California")
    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()
