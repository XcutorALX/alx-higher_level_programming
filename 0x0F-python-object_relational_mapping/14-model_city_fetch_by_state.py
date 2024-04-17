#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                            )

    Base.metadata.create_all(engine)
    session = Session(engine)

    query = select(City.name, City.id, State.name)\
        .join(State)\
        .order_by(City.id)
    result = session.execute(query).all()

    for row in result:
        print("{}: ({}) {}".format(row[2], row[1], row[0]))
