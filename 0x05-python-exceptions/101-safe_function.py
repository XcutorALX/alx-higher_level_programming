#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        result = None
    finally:
        return (result)

