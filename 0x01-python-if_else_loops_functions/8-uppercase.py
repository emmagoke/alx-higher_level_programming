#!/usr/bin/python3
def upper(c):
    return (chr(ord(c) - 32))

def uppercase(str):
    for i in str:
        if (ord(i) > 96) and (ord(i) < 123):
            i = upper(i)
        print("{}".format(i), end='')
    print()
