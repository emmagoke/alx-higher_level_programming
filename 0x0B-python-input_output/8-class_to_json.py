#!/usr/bin/python3
"""
This module contains class_to_json function
"""


def class_to_json(obj):
    """
    This function  returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    obj_dict = obj.__dict__
    return obj_dict
