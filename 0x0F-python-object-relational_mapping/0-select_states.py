#!/usr/bin/python3
import sys
import MySQLdb

"""This script lists all states from a database"""


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306, user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
