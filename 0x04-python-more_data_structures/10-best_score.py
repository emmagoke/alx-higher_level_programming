#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif len(a_dictionary) == 0:
        return None
    else:
        larg = sorted(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[larg]:
                larg = key
    return larg
