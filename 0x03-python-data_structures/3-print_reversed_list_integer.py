#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lens = len(my_list) - 1
    if not my_list:  # checks for empty list
        pass
    else:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
