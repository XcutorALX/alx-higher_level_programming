#!/usr/bin/python3
"""Lists all State objects and corresponding City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{username}:\
            {password}@localhost/{db_name}")

    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(State).join(State.cities)\
        .order_by(State.id, City.id)

    for state in states_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
