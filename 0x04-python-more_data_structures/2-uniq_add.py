#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    total = 0
    for col in my_list:
        if col not in seen:
            seen.add(col)
            total += col
    return total
