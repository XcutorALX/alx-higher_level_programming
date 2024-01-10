#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    toDelete = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            toDelete.append(key)

    for key in toDelete:
        a_dictionary.pop(key)

    return a_dictionary
