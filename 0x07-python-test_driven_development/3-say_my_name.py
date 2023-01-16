#!/usr/bin/python3
"""
This modeule contains say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    THis function print the first and the lastname.
    Argument:
        @first_name: The first argument.
        @last_name: The secnd argument,
        default to empty string.
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
