#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_l = len(row) - 1
        con = 0
        for col in row:
            if con < row_l:
                print("{:d}".format(col), end=' ')
                con += 1
            elif con == (row_l - 1):
                print("{:d}".format(col))
