#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for col in my_list:
        if col == search:
            result.append(replace)
        else:
            result.append(col)

    return result
