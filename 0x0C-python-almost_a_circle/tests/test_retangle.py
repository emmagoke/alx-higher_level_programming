#!/usr/bin/python3
"""
This file contains the test for the rectangle model.
"""
import unittest


class TestRectangle(unittest.TestCase):
    """
    This class test all the functionality of
    the Rectangle class.
    """

    def test_base(self):
        """
        Test the base method.
        """
        self.assertEqual(2 * 3 , 6)
