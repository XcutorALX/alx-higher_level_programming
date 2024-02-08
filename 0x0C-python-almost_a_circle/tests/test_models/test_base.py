#!/usr/bin/python3
"""Test case for Base class in models/base.py"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Test class for the base class"""

    def test_none(self):
        """Initialize an instance without id"""
        test = Base()
        self.assertEqual(1, test.id)

    def test_id(self):
        """Initialize an instance with specified id"""
        test = Base(9)
        self.assertEqual(9, test.id)
