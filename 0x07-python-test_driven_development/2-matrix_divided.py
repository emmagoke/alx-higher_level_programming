#!/usr/bin/python3
"""
This module contains matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    """
    len_mat = len(matrix) # number of rows
    for row in matrix:
        if type(row) != list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for col in row:
            if type(col) not in [float, int]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for i in range(len_mat - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = [[] for i in range(len_mat)]
    index = 0
    for row in matrix:
        for col in row:
            result[index].append(round(col / div, 2))
        index += 1

    return result
