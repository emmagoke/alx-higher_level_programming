#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(args[0], args[1])
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))

    return result
