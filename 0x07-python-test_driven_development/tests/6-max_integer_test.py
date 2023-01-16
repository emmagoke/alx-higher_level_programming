#!/usr/bin/python3
"""This is the test Module for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer



list_test = [1, 8, 9, 12, 3, 5]
class TestMaxInteger(unittest.TestCase):
    """
    This class contains the unit test for the max_integer function
    """

    def test_integer_list(self):
        """
        Testing for a list.
        """
        self.assertEqual(max_integer(list_test), 12)

    def test_empty_list(self):
        """This method tests for the empty list.
        """
        self.assertEqual(max_integer([]), None)

    def test_one_item(self):
        """
        Testing for one Item.
        """
        self.assertEqual(max_integer([3]), 3)

