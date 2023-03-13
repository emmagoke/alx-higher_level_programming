#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    This function deletes keys with a specific value
    in a dictionary.
    """
    key_ = []
    for key, val in a_dictionary.items():
        if val == value:
            key_.append(key)
    if key_:
        for key in key_:
            del a_dictionary[key]
    return a_dictionary
