#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        if not row:
            break
        for num in range(len(row)):
            print("{:d}".format(row[num]), end='')
            if num != len(row) - 1:
                print(" ", end='')
            else:
                print()
