#!/usr/bin/python3
"""This module contains a Base class"""
import json
import csv
import turtle
from random import randint


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

    @classmethod
    def load_from_file_csv(cls):
        """Loads csv representation of cls from <cls.__name__>.csv"""

        try:
            with open(cls.__name__ + '.csv',
                      encoding='utf-8', newline='') as csvfile:
                list_obj = []
                reader = csv.DictReader(csvfile, fieldnames=cls.attributes())
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])

                    list_obj.append(row)

                intances = [cls.create(**i) for i in list_obj]
                return (intances)
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a class instance to a csv file named <cls.__name.__>.csv"""
        filename = cls.__name__ + ".csv"

        with open(filename, encoding='utf-8',
                  mode='a+', newline='') as csvfile:

            prev_list = []
            csvfile.seek(0)
            reader = csv.DictReader(csvfile, fieldnames=cls.attributes())

            prev_list = [i for i in reader]

            if list_objs is None:
                new_list = []
            else:
                new_list = [i.to_dictionary() for i in list_objs]

            prev_list += new_list
            csvfile.seek(0)
            csvfile.truncate()
            writer = csv.DictWriter(csvfile, fieldnames=cls.attributes())

            for row in prev_list:
                writer.writerow(row)

    @staticmethod
    def dummyInstance():
        """Creates a dummy instance of the base class"""

        return (Base())

    @staticmethod
    def draw(list_rectangles, list_squares):
        if list_rectangles in [None, []] or list_squares in [None, []]:
            return

        t = turtle.Turtle()
        t.color("Black")
        turtle.colormode(255)
        for rect in list_rectangles + list_squares:
            t.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
            t.begin_fill()
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.end_fill()

        t.screen.mainloop()
