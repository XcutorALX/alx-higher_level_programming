#!/usr/bin/python3
def safe_print_integer(value):
    if (value is None or value is True or value is False):
        return (False)
    try:
        print("{:d}".format(value))
    except ValueError:
        return (False)

    return (True)
