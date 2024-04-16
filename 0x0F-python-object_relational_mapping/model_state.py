#!/usr/bin/python3
""" This script that lists all states
from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):

    __tablename__ = "states"
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False
        )
    name = Column(
                String(128),
                nullable=False
            )
