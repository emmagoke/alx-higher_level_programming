#!/usr/bin/python3
def int_to_str(i):
    string = ''
    while True:
        i , remainder = divmod(i, 10)
        string += chr(ord('0') + remainder)
        if i == 0:
            break
    return string


def print_list_integer(my_list=[]):
    lens = len(my_list)
    for i in range(lens):
        val = int_to_str(i)
        print(str.format(val))
