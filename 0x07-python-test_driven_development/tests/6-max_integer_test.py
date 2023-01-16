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

    def test_max_end(self):
        """
        Testing for maximum number at the end of the list.
        """
        self.assertEqual(max_integer(list_test[:4]), 12)

    def test_max_at_beginning(self):
        """
        Testing when the maximum number is at the beginning.
        """
        self.assertEqual(max_integer([19, 1, 4, 6]), 19)

    def test_one_negative_number(self):
        """One nea=gative number in the list
        """
        self.assertEqual(max_integer([10, -5, 8, 16, 11]), 16)

    def test_all_negative_number(self):
        """All the list are negative number
        """
        self.assertEqual(max_integer([-1, -4, -7, -10]), -1)

