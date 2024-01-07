#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in range(len(row)):
            if num == 0:
                break

            print("{:d}".format(row[num]), end='')
            if num != len(row) - 1:
                print(" ", end='')
            else:
                print()
