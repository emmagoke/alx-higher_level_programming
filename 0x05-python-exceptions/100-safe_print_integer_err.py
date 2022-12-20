#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    out = False
    try:
        print("{:d}".format(value))
        out = True
    except Exception as error:
        print(error, file=sys.stderr)
    return out
