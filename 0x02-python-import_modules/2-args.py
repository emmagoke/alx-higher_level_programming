#!/usr/bin/python3
from sys import argv

l = len(argv) - 1

if l == 0:
    print("{} arguments.".format(l))
elif l > 0:
    print("{} arguments.".format(l))
    for i in range(1, (l + 1)):
        print("{}: {}".format(i, argv[i]))

