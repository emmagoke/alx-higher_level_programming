#!/usr/bin/python3
"""
This module contains the add_attribute function
which checks if a class has the attribute
"""
def add_attribute(cls, attr, value):
    """
    This function checks if attr is an attribute
    of cls
    args:
        cls: class
        attr: attribute
        value: value
    """
    if hasattr(cls, attr):
        raise TypeError("can't add new attribute")
    setattr(cls, attr, value)
