#!/usr/bin/python3
"""Test module for the Square class in the square module"""
import unittest
import sys
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):
    """Test Square"""

    def test_module_docstring(self):
        """Test the docstring of the module"""

        info = __import__("models").square.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_class_docstring(self):
        """Tests the docstring of the class"""
        info = Square.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_withGoodInput(self):
        """Testing an instance with good input"""

        test = Square(5, 3, 2)
        test2 = Square(2)
        self.assertEqual(test2.x, 0)
        self.assertEqual(test.width, 5)
        self.assertEqual(test.height, 5)
        self.assertEqual(test.x, 3)
        self.assertEqual(test.y, 2)

    def test_size_docstring(self):
        """Testing the docstring of the size method"""

        info = Square.size.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_size_setter(self):
        """Testing the size setter and getter"""

        test = Square(4, 6, 3, 8)
        self.assertEqual(test.size, 4)
        test.size = 6
        self.assertEqual(test.size, 6)

        output = "width must be an integer"
        with self.assertRaisesRegex(TypeError, output):
            test.size = [2, 5]

        with self.assertRaisesRegex(TypeError, output):
            test.size = (2, 3)

        with self.assertRaisesRegex(TypeError, output):
            test.size = None
        output = "width must be > 0"
        with self.assertRaisesRegex(ValueError, output):
            test.size = -1

    def test_x_setter(self):
        """Testing the x setter and getter"""

        test = Square(4, 6, 3, 8)
        self.assertEqual(test.x, 6)
        test.x = 8
        self.assertEqual(test.x, 8)

        output = "x must be an integer"
        with self.assertRaisesRegex(TypeError, output):
            test.x = [2, 5]

        with self.assertRaisesRegex(TypeError, output):
            test.x = (2, 3)

        with self.assertRaisesRegex(TypeError, output):
            test.x = None
        output = "x must be >= 0"
        with self.assertRaisesRegex(ValueError, output):
            test.x = -1

    def test_y_setter(self):
        """Testing the y setter and getter"""

        test = Square(4, 6, 3, 8)
        self.assertEqual(test.y, 3)
        test.y = 8
        self.assertEqual(test.y, 8)

        output = "y must be an integer"
        with self.assertRaisesRegex(TypeError, output):
            test.y = [2, 5]

        with self.assertRaisesRegex(TypeError, output):
            test.y = (2, 3)

        with self.assertRaisesRegex(TypeError, output):
            test.y = None
        output = "y must be >= 0"
        with self.assertRaisesRegex(ValueError, output):
            test.y = -2

    def test_id(self):
        """Testing the id of the rectangle class"""

        Square.resetId()
        r1 = Square(4, 5, 9, 2)
        r2 = Square(3, 5, 3)
        r3 = Square(2, 4, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r3.id, 2)

    def test_area_docstring(self):
        """Testing the docstring of the area method"""

        info = Square.area.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_area(self):
        """Testing the area method"""

        r1 = Square(2, 5, 7)
        self.assertEqual(r1.area(), 4)

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

    def test_display_docstring(self):
        """Testing the docstring of the display method"""
        info = Square.display.__doc__
        self.assertTrue(len(info) > 1, True)

    def test_display(self):
        """Testint the display method"""

        r1 = Square(4)
        result = self.capture_stdout(r1.display)
        self.assertEqual(result.getvalue(), "####\n####\n####\n####\n")
        r2 = Square(3, 2, 3)
        result = self.capture_stdout(r2.display)
        self.assertEqual(result.getvalue(), "\n\n\n  ###\n  ###\n  ###\n")

    def test_print(self):
        """Tests the __str__ representation"""

        r1 = Square(3, 3, 4, 9)
        result = self.capture_stdout(print, r1)
        self.assertEqual(result.getvalue(), "[Square] (9) 3/4 - 3\n")

    def test_update_docstring(self):
        """Testing the docstring of the area method"""
        info = Square.update.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_update(self):
        """Tests the update method of Rectangle"""

        Square.resetId()
        r1 = Square(5, 6, 8, 2)
        r1.update(4, 2, 7, 8, id=7)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r1.id, 4)
        r1.update(size=10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.width, 10)

    def test_to_dictionary_docstring(self):
        """Testing the docstring of the to dictionary method"""
        info = Square.to_dictionary.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_to_dictionary(self):
        """testing the dictionary representation"""

        r1 = Square(4, 5, 4, 2)
        result = {'size': 4, 'x': 5, 'y': 4, 'id': 2}
        self.assertEqual(r1.to_dictionary(), result)

    def test_dummyInstance_docstring(self):
        """Testing the docstring of the dummyInstance method"""

        info = Square.dummyInstance.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_dummyInstance(self):
        """Testing the dummyInstance method"""
        Square.resetId()
        test = Square.dummyInstance()
        self.assertEqual(test.size, 1)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.id, 1)
        self.assertEqual(type(test), Square)

    def test_attributes_docstring(self):
        """Testing the docstring of the attributes method"""
        info = Square.attributes.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_attributes(self):
        """Testing the attributes method of the Square class"""
        result = ['id', 'size', 'x', 'y']
        output = Square.attributes()
        self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
