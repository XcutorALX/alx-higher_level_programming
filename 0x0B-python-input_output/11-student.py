#!/usr/bin/python3
"""This module contains a student class"""


class Student:
    """Object representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Instantizes an object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dict representation of a student instance"""

        if type(attrs) == list and (type(i) == str for i in attrs):
            res = dict()
            for i in attrs:
                if i in self.__dict__:
                    res[i] = self.__dict__[i]

            return (res)

        return (self.__dict__)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for i in json:
            self.__setattr__(i, json[i])
