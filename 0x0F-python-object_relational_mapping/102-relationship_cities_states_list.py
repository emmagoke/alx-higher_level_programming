#!/usr/bin/python3
"""
This python script lists all City objects from the database hbtn_0e_101_usa
Usage : ./102-relationship_cities_states_list.py <mysql username>
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

    query = session.query(City).order_by(City.id).all()
    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
