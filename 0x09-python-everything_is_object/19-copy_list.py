#!/usr/bin/python3
def copy_list(l):
    return (l[:] if type(l) == list else [])
