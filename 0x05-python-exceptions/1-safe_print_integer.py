#!/usr/bin/python3
def safe_print_integer(value):
    out = True
    try:
        print("{:d}".format(value))
    except ValueError:
        out = False
    finally:
        return out
