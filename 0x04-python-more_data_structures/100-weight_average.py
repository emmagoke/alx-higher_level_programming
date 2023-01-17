#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    this function returns the weighted average
    of all integers tuple (<score>, <weight>)
    """
    result = 0
    if len(my_list) == 0:
        return result
    den = 0
    for item in my_list:
        den += item[1]
        result += (item[0] * item[1])
    result = result / den
    return result
