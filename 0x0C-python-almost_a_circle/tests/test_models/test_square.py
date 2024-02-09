#!/usr/bin/python3
"""Test module for the Square class in the square module"""
import unittest
import sys
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):
    """Test Square"""

    def test_withGoodInput(self):
        """Testing an instance with good input"""

        test = Square(5, 3, 2)
        test2 = Square(2)
        self.assertEqual(test2.x, 0)
        self.assertEqual(test.width, 5)
        self.assertEqual(test.height, 5)
        self.assertEqual(test.x, 3)
        self.assertEqual(test.y, 2)
    
    def test_setters(self):
        """Testing the setters of Rectangle"""

        test = Square(4, 6, 3, 2)
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
        r2 = Rectangle(3, 4, 2, 3)
        result = self.capture_stdout(r2.display)
        self.assertEqual(result.getvalue(), "\n\n\n  ###\n  ###\n  ###\n  ###\n")

    def test_print(self):
        """Tests the __str__ representation"""
        
        r1 = Rectangle(2, 3, 3, 4 , 9)
        result = self.capture_stdout(print, r1)
        self.assertEqual(result.getvalue(), "[Rectangle] (9) 3/4 - 2/3\n")

    def test_update(self):
        """Tests the update method of Rectangle"""

        Rectangle.resetId()
        r1 = Rectangle(2, 3, 5, 6, 8)
        r1.update(1, 4, 2, 7, 8, id=7)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r1.id, 1)
        r1.update(width=10, height=20)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.width, 10)

if __name__ == "__main__":
    unittest.main()
