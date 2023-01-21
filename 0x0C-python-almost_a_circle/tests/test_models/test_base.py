#!/usr/bin/python
"""This module contains all the
test cases for models/base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This class contains all the method to test base
    """

    def test_base_with_id(self):
        """
        This method test Base with an id.
        """
        b1 = Base(10)
        b2 = Base(13)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 13)

    def test_base_it_id_and_none(self):
        """
        THis method tests Base with id
        and with None.
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

