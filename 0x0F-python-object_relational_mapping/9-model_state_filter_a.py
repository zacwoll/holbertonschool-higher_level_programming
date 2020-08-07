#!/usr/bin/python3
""" lists all State objects that contain the letter a from the database """

from model_state import State, Base
from sqlalchemy import (create_engine, Table, Integer, String, Column)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    a_list = session.query(State).order_by(State.id).filter(
        State.name.like("%a%"))
    for a_name in a_list:
        print("{}: {}".format(a_name.id, a_name.name))
    session.close()
