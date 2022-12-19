#!/usr/bin/python3
def safe_print_integer(value):
    out = True
    try:
        print("{:d}".format(value))
    except Exception:
        out = False
    finally:
        return out
