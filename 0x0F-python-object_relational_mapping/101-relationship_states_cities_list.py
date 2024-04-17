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

    states_cities = session.query(State, City).join(City)\
        .order_by(State.id, City.id)

    current_state_id = None
    for state, city in states_cities:
        if state.id != current_state_id:
            print(f"{state.id}: {state.name}")
            current_state_id = state.id
        print(f"    {city.id}: {city.name}")

    session.close()
