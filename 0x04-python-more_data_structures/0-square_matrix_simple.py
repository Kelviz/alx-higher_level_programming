#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        x = []
        for n in i:
            sq_n = n*n
            x.append(sq_n)
        new_matrix.append(x)
    return new_matrix
