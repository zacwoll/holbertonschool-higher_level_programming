#!/usr/bin/python3
""" Lists all State objects and corresponding City objects """

from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine, Table, Integer, String, Column
from sqlalchemy.orm import sessionmaker
from sys import argv

# Args: (mysql_user, mysql_pass, db_name, state_name_to_search)
if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
