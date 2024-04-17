#!/usr/bin/python3
""" This script that lists all states
from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    class representation of a city
    """
    __tablename__ = "cities"
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
    state_id = Column(
                Integer,
                ForeignKey('states.id'),
                nullable=False,
            )
