#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        stderr.write("Exception: {}\n".format(err))
        return (False)
    except TypeError as err:
        stderr.write("Exception: {}\n".format(err))
        return (False)

    return(True)
