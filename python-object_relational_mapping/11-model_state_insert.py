#!/usr/bin/python3
""" Python script that adds the State object
    “Louisiana” in the db
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
