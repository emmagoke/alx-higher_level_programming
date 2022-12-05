#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lens = len(my_list) - 1
    for i in range(lens, -1, -1):
        print("{:d}".format(my_list[i]))
