#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    This function adds all unique integers in a list
    (only once for each integer).
    """
    out = []
    sum_u = 0
    for i in my_list:
        if i  not in out:
            sum_u += i
            out.append(i)
    return sum_u
