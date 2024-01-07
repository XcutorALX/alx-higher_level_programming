#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = []
    for i in range(2):
        if len(tuple_a) - 1 < i and len(tuple_b) - 1 < i:
            new.append(0)
        elif len(tuple_a) - 1 < i:
            new.append(0 + tuple_b[i])
        elif len(tuple_b) - 1 < i:
            new.append(0 + tuple_a[i])
        else:
            new.append(tuple_a[i] + tuple_b[i])

    return tuple(new)
