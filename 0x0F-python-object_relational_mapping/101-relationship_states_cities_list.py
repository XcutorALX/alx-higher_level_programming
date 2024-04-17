#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                            )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for row in result:
        print("{}: {}".format(row.id, row.name))
        for city in row.cities:
            print("    {}: {}".format(city.id, city.name))
