#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                            )

    Base.metadata.create_all(engine)
    session = Session(engine)
    query = select(State.id, State.name).order_by(State.id)

    result = session.execute(query).first()

    if result is not None:
        print("{}: {}".format(result[0], result[1]))
    else:
        print("Nothing")
