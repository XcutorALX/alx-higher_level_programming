#!/usr/bin/python3
"""Test case for Base class in models/base.py"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test class for the base class"""

    def test_modele_docstring(self):
        """Testing the module docstring"""
        info = __import__("models").base.__doc__

        self.assertEqual(len(info) > 1, True)

    def test_class_docstring(self):
        """Teesting the Base class docstring"""
        info = Base.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_reset_id_docstring(self):
        """Testing the reset id method docstring"""
        info = Base.resetId.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_none(self):
        """Initialize an instance without id"""
        Base.resetId()
        test = Base()
        self.assertEqual(1, test.id)

    def test_id(self):
        """Initialize an instance with specified id"""
        Base.resetId()
        test = Base(9)
        self.assertEqual(9, test.id)

    def test_to_json_string_docstring(self):
        """Testing the docstring of the to json string method"""
        info = Base.to_json_string.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_to_json_string(self):
        """Tests the to json string method of the Base class"""

        Base.resetId()
        test = {'x': 7, 'y': 10, 'size': 14}
        result = '{"x": 7, "y": 10, "size": 14}'
        self.assertEqual(Base.to_json_string(test), result)
        self.assertEqual(Base.to_json_string({}), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_docstring(self):
        """Tests the docstring of the to json string method"""

        info = Base.from_json_string.__doc__
        self.assertEqual(len(info) > 1, True)

    def from_json_string(self):
        """Tests the from json string method of the Base class"""

        Base.resetId()
        test = '{"x": 7, "y", 8, "size", 9}'
        result = {"x", 7, "y", 8, "size", 9}
        self.assertEqual(Base.from_json_string(test), result)
        self.assertEqual(Base.from_json_string("[]", []))
        self.assertEqual(Base.from_json_string(None, []))

    def test_save_to_file_docstring(self):
        """Tests the docstring of the save to file method"""
        info = Base.save_to_file.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_save_to_file(self):
        """Tests the save to file method of the Base class"""

        Base.resetId()
        f = open("Rectangle.json", mode="w")
        f.close()

        r1 = Rectangle(4, 5, 3, 2, 1)
        r2 = Rectangle(5, 6, 7, 8, 9)
        r3 = Rectangle(3, 4, 6, 8)
        r1.save_to_file([r1, r2])
        r3.save_to_file([r3])
        r3.save_to_file(None)
        r3.save_to_file([])

        with open("Rectangle.json", encoding='utf-8') as f:
            self.assertEqual(json.load(f),
                             [i.to_dictionary() for i in [r1, r2, r3]])

        f = open("Square.json", mode="w")
        f.close()

        s1 = Square(5, 6, 7, 1)
        s2 = Square(3, 2, 1, 8)
        s3 = Square(4, 5, 2, 5)
        s1.save_to_file([s1, s2])
        s3.save_to_file([s3])

        with open("Square.json", encoding='utf-8') as f:
            self.assertEqual(json.load(f),
                             [i.to_dictionary() for i in [s1, s2, s3]])

    def test_create_docstring(self):
        """Tests the docstring of the create method"""
        info = Base.create.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_create(self):
        """Tests the create method of the Base class"""
        Base.resetId()
        test = Square.create(size=7, x=8, y=4, id=2)
        result = "[Square] (2) 8/4 - 7"
        self.assertEqual(str(test), result)

    def test_load_from_file_docstring(self):
        """Tests the docstring of the load from file method"""
        info = Base.load_from_file.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_load_from_file(self):
        """Tests the load from file method of the Base class"""
        Base.resetId()
        r1 = Rectangle(4, 5, 3, 2, 1)
        r2 = Rectangle(5, 6, 7, 8, 9)
        r3 = Rectangle(3, 4, 6, 8)
        with open("Rectangle.json", mode="w") as f:
            pass
        r1.save_to_file([r1, r2, r3])
        inst = [str(i) for i in Rectangle.load_from_file()]

        self.assertEqual(str(r1), inst[0])
        self.assertEqual(str(r2), inst[1])
        self.assertEqual(str(r3), inst[2])

        s1 = Square(5, 6, 7, 1)
        s2 = Square(3, 2, 1, 8)
        s3 = Square(4, 5, 2, 5)
        with open("Square.json", mode="w") as f:
            pass

        s3.save_to_file([s1, s2, s3])
        inst = [str(i) for i in Square.load_from_file()]
        self.assertEqual(str(s1), inst[0])
        self.assertEqual(str(s2), inst[1])
        self.assertEqual(str(s3), inst[2])

    def test_greaterThanValidator_docstring(self):
        """Tests the docstring for the greater than validator method"""

        info = Base.greaterThanValidator.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_greaterThanValidator(self):
        """Tests the greater than validator method"""

        with self.assertRaises(ValueError) as err:
            Base.greaterThanValidator("test", 5, 8)
            self.assertEqual(err.exception, "test must be >= 8")

        Base.greaterThanValidator("test", 5, 2)

    def test_greaterOrEqual_docstring(self):
        """Tests the docstring for the method"""

        info = Base.greaterOrEqualValidator.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_greaterOrEqual(self):
        """Tests the greater or equal validator"""

        output = "test must be >= 7"
        with self.assertRaisesRegex(ValueError, output):
            Base.greaterOrEqualValidator("test", 5, 7)

        Base.greaterOrEqualValidator("test", 5, 5)

    def test_typeValidator_docstring(self):
        """Tests the docstring of the type validator"""
        info = Base.typeValidator.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_typeValidator(self):
        """Tests the type validator"""

        output = "test must be an integer"
        with self.assertRaisesRegex(TypeError, output):
            Base.typeValidator("test", "str")

        Base.typeValidator("test", 8)

    def test_dummyInstance_docstring(self):
        """Testing the docstring for the dummy instance method"""

        test = Base.dummyInstance.__doc__
        self.assertEqual(len(test) > 1, True)

    def test_dummyInstance(self):
        """Tests the dummy instance method of the base class"""

        Base.resetId()
        test = Base.dummyInstance()
        self.assertEqual(test.id, 1)
