#!/usr/bin/python3
"""
This python file prints all City objects from the database hbtn_0e_14_usa
in this format: <state name>: (<city id>) <city name>
Usage : ./14-model_city_fetch_by_state.py <mysql username>
                                          <mysql password>
                                          <database name>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import State

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).order_by(City.id).all()
    for city in query:
        print(f"{city.state.name}: ({city.id}) {city.name}")
    session.close()
