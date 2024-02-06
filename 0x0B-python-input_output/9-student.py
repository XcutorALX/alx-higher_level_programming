#!/usr/bin/python3
"""This module contains a student class"""


class Student:
    """Object representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Instantizes an object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dict representation of a student instance"""
        return (self.__dict__)
