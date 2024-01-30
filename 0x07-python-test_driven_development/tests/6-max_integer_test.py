#!/usr/bin/python3
"""Unittest for max integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Suite test for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([3, 43, 51, 85, -2]), 85)

    def test_empty_list(self):
        self.assertEqualmax_integer([]), None)

    def test_string_list(self):
        self.assertRaises(max_integer([19, 'tunde']), TypeError)

    def test_single_list(self):
        self.asserEqual(max_integer([4]), 4)

    def test_repeated_list(self):
        self.assertEqual(max_integer([9, 9, 9, 9]), 9)
    
    def test_tuple_in_list(self):
        self.assertRaises(max_integer([4, (3, 4)]), TypeError)

    def test_boolean(self):
        self.assertRaises(max_integer([True, 6]), TypeError)

    def test_dictionary_in_list:
        self.assertRaises(max_integer([5, {"kay": 7}]), TypeError)

    def test_dictionary:
        self.assertRaises(max_integer({"kay": 9}), TypeError)

    def test_number:
        self.assertRaises(max_integer(7), TypeError)
