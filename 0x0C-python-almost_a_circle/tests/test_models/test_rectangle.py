#!/usr/bin/python3
"""Test module for the Rectangle class in rectangle.py"""
import unittest
import sys
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Test Rectangle"""

    def test_module_docstring(self):
        info = __import__("models").rectangle.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_class_docstring(self):
        info = Rectangle.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_withGoodInput(self):
        """Testing an instance with good input"""

        test = Rectangle(5, 6, 3, 2)
        test2 = Rectangle(2, 3)
        self.assertEqual(test2.x, 0)
        self.assertEqual(test.width, 5)
        self.assertEqual(test.height, 6)
        self.assertEqual(test.x, 3)
        self.assertEqual(test.y, 2)

    def test_width_setter_docstring(self):
        info = Rectangle.width.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_height_setter_docstring(self):
        info = Rectangle.height.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_x_setter_docstring(self):
        info = Rectangle.x.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_y_setter_docstring(self):
        info = Rectangle.y.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_update_docstring(self):
        info = Rectangle.update.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_x_setter_and_getter(self):
        """Testing the x setter and getter"""
        Rectangle.resetId()
        test = Rectangle(5, 6, 2, 1, 9)
        self.assertEqual(test.x, 2)
        test.x = 10
        self.assertEqual(test.x, 10)

        output = "x must be an integer"
        with self.assertRaisesRegex(TypeError, output):
            test.x = "str"

        with self.assertRaisesRegex(TypeError, output):
            test.x = [1, 2, 3]

        with self.assertRaisesRegex(TypeError, output):
            test.x = None

        output = "x must be >= 0"
        with self.assertRaisesRegex(ValueError, output):
            test.x = -1

    def test_y_setter_and_getter(self):
        """Testing the y setter and getter"""
        Rectangle.resetId()
        test = Rectangle(5, 6, 2, 1, 9)
        self.assertEqual(test.y, 1)
        test.y = 10
        self.assertEqual(test.y, 10)

        output = "y must be an integer"
        with self.assertRaisesRegex(TypeError, output):
            test.y = "str"

        with self.assertRaisesRegex(TypeError, output):
            test.y = [1, 2, 3]

        with self.assertRaisesRegex(TypeError, output):
            test.y = None

        output = "y must be >= 0"
        with self.assertRaisesRegex(ValueError, output):
            test.y = -1

    def test_width_setter_and_getter(self):
        """Testing the width setter and getter"""
        Rectangle.resetId()
        test = Rectangle(5, 6, 2, 1, 9)
        self.assertEqual(test.width, 5)
        test.width = 10
        self.assertEqual(test.width, 10)

        output = "width must be an integer"
        with self.assertRaisesRegex(TypeError, output):
            test.width = "str"

        with self.assertRaisesRegex(TypeError, output):
            test.width = [1, 2, 3]

        with self.assertRaisesRegex(TypeError, output):
            test.width = None

        output = "width must be > 0"
        with self.assertRaisesRegex(ValueError, output):
            test.width = -1

    def test_height_setter_and_getter(self):
        """Testing the x setter and getter"""
        Rectangle.resetId()
        test = Rectangle(5, 6, 2, 1, 9)
        self.assertEqual(test.height, 6)
        test.height = 10
        self.assertEqual(test.height, 10)

        output = "height must be an integer"
        with self.assertRaisesRegex(TypeError, output):
            test.height = "str"

        with self.assertRaisesRegex(TypeError, output):
            test.height = [1, 2, 3]

        with self.assertRaisesRegex(TypeError, output):
            test.height = None

        output = "height must be > 0"
        with self.assertRaisesRegex(ValueError, output):
            test.height = -1

    def test_id(self):
        """Testing the id of the rectangle class"""

        Rectangle.resetId()
        r1 = Rectangle(4, 5, 9, 2)
        r2 = Rectangle(3, 5, 3, 1, 5)
        r3 = Rectangle(2, 4, 1, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r3.id, 2)

    def test_area_docstring(self):
        """Testing the area method docstring"""

        info = Rectangle.area.__doc__
        self.assertEqual(len(info) > 1, True)

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

    def test_display_docstring(self):
        """Testing the ddocstring for the display method"""

        info = Rectangle.display.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_display(self):
        """Testint the display method"""

        r1 = Rectangle(4, 5)
        result = self.capture_stdout(r1.display)
        self.assertEqual(result.getvalue(), "####\n####\n####\n####\n####\n")
        r2 = Rectangle(3, 4, 2, 3)
        result = self.capture_stdout(r2.display)
        self.assertEqual(result.getvalue(),
                         "\n\n\n  ###\n  ###\n  ###\n  ###\n")

    def test_print(self):
        """Tests the __str__ representation"""

        r1 = Rectangle(2, 3, 3, 4, 9)
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

    def test_to_dictionary_docstring(self):
        """Testing the docstring for the to dictionary method"""

        info = Rectangle.to_dictionary.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_to_dictionary(self):
        """Testing the to dictionary method for the Rectangle class"""

        r1 = Rectangle(4, 5, 6, 7, 8)
        result = {'width': 4, 'height': 5, 'x': 6, 'y': 7, 'id': 8}
        self.assertEqual(r1.to_dictionary(), result)

    def test_dummyInstance_docstring(self):
        """Testing the docstring for the dummy instance method"""

        info = Rectangle.dummyInstance.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_dummyInstance(self):
        """Testing the dummy instance for the Rectangle class"""

        Rectangle.resetId()
        test = Rectangle.dummyInstance()
        self.assertEqual(test.width, 1)
        self.assertEqual(test.height, 1)
        self.assertEqual(test.x, 0)
        self.assertEqual(test.y, 0)
        self.assertEqual(test.id, 1)

    def test_attributes_docstring(self):
        """Testing the docstring of the attributes method"""
        info = Rectangle.attributes.__doc__
        self.assertEqual(len(info) > 1, True)

    def test_attributes(self):
        """Testing the attribute method of the Rectangle class"""
        result = ['id', 'width', 'height', 'x', 'y']
        output = Rectangle.attributes()
        self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
