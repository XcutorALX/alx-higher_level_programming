#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted([i for i in a_dictionary])
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
