#!/usr/bin/python3
""" This script that lists all states
from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )

    cur = db.cursor()
    cur.execute(
            "SELECT cities.name FROM cities\
            WHERE cities.state_id IN (\
                SELECT states.id FROM states\
                WHERE states.name = (%s)\
                )\
            ORDER BY cities.id", (sys.argv[4],)
            )
    cities = cur.fetchall()

    city_names = ', '.join(city[0] for city in cities)
    print(city_names)

    cur.close()
    db.close()
