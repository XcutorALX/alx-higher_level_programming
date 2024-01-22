#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0

    if (!my_list or x < 0):
        return (0)

    while (i < x):
        try:
            print(my_list[i], end='')
        except IndexError:
            print()
            return (i)
        except TypeError:
            print()
            return (i);
        i += 1
    print()
    return (i)
