#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]

    if len(my_list) == 0:
        return (None)

    for num in my_list:
        if num > largest:
            largest = num

    return (largest)
