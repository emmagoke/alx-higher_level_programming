#!/usr/bin/python3
"""
This module contains load_from_json_file function
"""
import json



def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”.
    """
    with open(filename, encoding="utf-8") as myfile:
        content = json.load(myfile)
    return content
