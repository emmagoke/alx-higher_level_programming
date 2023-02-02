#!/usr/bin/python3

def add_attribute(cls, attr, value):
    """
    """
    if hasattr(cls, attr):
        raise TypeError("can't add new attribute")
    setattr(cls, attr, value)
