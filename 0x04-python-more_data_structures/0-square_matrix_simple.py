#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [[] for i in matrix]
    for row in range(len(matrix)):
        for col in matrix[row]:
            square[row].append(col * col)
    return square
