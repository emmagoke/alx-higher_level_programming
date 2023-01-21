#!/usr/bin/python3
"""
This module has the test for the Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class has methods that test the Rectangle class
    """

    def test_with_all_attribute(self):
        """
        Test Rectangle with all attribute.
        """
        rect = Rectangle(10, 10, 2, 5, 9)
        self.assertEqual(rect.id, 9)

    def test_called_with_one_attribute(self):
        """
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(10)

    def test_called_with_no_attribute(self):
        """
        """
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_called_two_attribute(self):
        """
        """
        r1 = Rectangle(10, 15)
        r2 = Rectangle(15, 10)
        self.assertEqual(r2.id, 4)

