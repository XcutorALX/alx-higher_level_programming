#!/usr/bin/python3
"""This module contains a Base class"""
import json


class Base:
    """Base class of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantizes a Base class with the specified ID"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def typeValidator(name, value):
        """Checks if value if of type int"""

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        return (1)

    @staticmethod
    def greaterThanValidator(name, value, test):
        """Checks if value > test"""

        if value <= test:
            raise ValueError(f"{name} must be > {test}")

        return (1)

    @staticmethod
    def greaterOrEqualValidator(name, value, test):
        """Checks if value >= test"""

        if value < test:
            raise ValueError(f"{name} must be >= {test}")

        return (1)

    @staticmethod
    def resetId():
        """Resets the id of the Base class"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == {}:
            return ('[]')

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to file"""

        name = cls.__name__ + '.json'
        with open(name, encoding='utf-8', mode='a+') as f:
            new_list = []
            prev_list = []

            f.seek(0)
            string = f.read()

            if string:
                f.seek(0)
                prev_list = json.load(f)

            if list_objs is None:
                new_list = []
            else:
                new_list = [i.to_dictionary() for i in list_objs]

            prev_list += new_list
            f.seek(0)
            f.truncate()
            f.write(Base.to_json_string(prev_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation of json_string"""

        if json_string in [None, ""]:
            return ([])

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        new = cls.dummyInstance()
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """Loads json string from file and returns a list of instances"""

        try:
            with open(cls.__name__ + '.json', encoding='utf-8') as f:
                jsonStr = f.read()
                dict_list = Base.from_json_string(jsonStr)
                instances = [cls.create(**i) for i in dict_list]
                return (instances)
        except IOError:
            return []

    @staticmethod
    def dummyInstance():
        """Creates a dummy instance of the base class"""

        return (Base())
