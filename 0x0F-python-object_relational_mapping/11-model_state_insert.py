#!/usr/bin/python3
""" adds 'Louisiana; to the database """

from model_state import State, Base
from sqlalchemy import (create_engine, Table, Integer, String, Column)
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

    state = State(name="Louisiana")
    session.add(state)
    session.flush()
    print(state.id)
    session.commit()
    session.close()
