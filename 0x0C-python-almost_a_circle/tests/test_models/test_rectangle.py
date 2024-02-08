#!/usr/bin/python3
"""Test module for the Rectangle class in rectangle.py"""
import unittest
import sys
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Test Rectangle"""

    def test_withGoodInput(self):
        """Testing an instance with good input"""

        test = Rectangle(5, 6, 3, 2)
        test2 = Rectangle(2, 3)
        self.assertEqual(test2.x, 0)
        self.assertEqual(test.width, 5)
        self.assertEqual(test.height, 6)
        self.assertEqual(test.x, 3)
        self.assertEqual(test.y, 2)
    
    def test_setters(self):
        """Testing the setters of Rectangle"""

        test = Rectangle(5, 6, 3, 2)
        test.width = 10
        self.assertEqual(test.width, 10)
        test.height = 15
        self.assertEqual(test.height, 15)
        test.x = 9
        self.assertEqual(test.x, 9)
        test.y = 8
        self.assertEqual(test.y, 8)

    def test_validator(self):
        """Testing the validators"""

        test = Rectangle(5, 6, 3, 2)
        with self.assertRaises(ValueError):
            test.height = False
        with self.assertRaises(ValueError):
            test.width = "random"
        with self.assertRaises(ValueError):
            test.x = (1, 2)
        with self.assertRaises(ValueError):
            test.y = [1, 2]
        with self.assertRaises(TypeError):
            test.height = 0
        with self.assertRaises(TypeError):
            test.width = -1
        with self.assertRaises(TypeError):
            test.x = -1
        test.y = 0
        self.assertEqual(test.y, 0)

    def test_id(self):
        """Testing the id of the rectangle class"""

        Rectangle.resetId()
        r1 = Rectangle(4, 5, 9, 2)
        r2 = Rectangle(3, 5, 3, 1, 5)
        r3 = Rectangle(2, 4, 1, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r3.id, 2)

    def test_area(self):
        """Testing the area method"""

        r1 = Rectangle(1, 2, 5, 7, 2)
        self.assertEqual(r1.area(), 2)

    @staticmethod
    def capture_stdout(displayFunc, arg=None):
        """captures stdout and returns stdout"""

        stream = StringIO()
        sys.stdout = stream

        if arg is None:
            displayFunc()
        else:
            displayFunc(arg)

        sys.stdout = sys.__stdout__
        return (stream)
        
    def test_display(self):
        """Testint the display method"""

        r1 = Rectangle(4, 5)
        result = self.capture_stdout(r1.display)
        self.assertEqual(result.getvalue(), "####\n####\n####\n####\n####\n")

if __name__ == "__main__":
    unittest.main()
