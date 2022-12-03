#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    lens = len(argv) - 1
    sums = 0
    for i in range(1, (lens + 1)):
        sums += int(argv[i])
    print("{}".format(sums))
