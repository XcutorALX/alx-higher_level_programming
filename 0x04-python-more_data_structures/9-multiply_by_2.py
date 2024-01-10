#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = dict()

    for key in a_dictionary:
        newDict[key] = a_dictionary[key] * 2

    return newDict
