#!/usr/bin/python3
"""
This module contains MyList Class
"""


class MyList(list):
    """
    MyList inheritance from the list class.
    """
    def print_sorted(self):
        """
        """
        li = self.copy()
        li = sorted(li)
        print(li)
