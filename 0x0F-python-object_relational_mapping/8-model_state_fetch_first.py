#!/usr/bin/python3
""" prints the first state object from hbtn_0e_6_usa """

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

    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
