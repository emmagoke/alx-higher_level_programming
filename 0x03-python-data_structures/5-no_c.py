#!/usr/bin/python3
def no_c(my_string):
    out = ''
    for i in my_string:
        if i not in 'cC':
            out += i
    return out
