#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lens = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            lens += 1
    except IndexError:
        lens += 0
    finally:
        print()
        return lens
