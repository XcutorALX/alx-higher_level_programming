#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0

    if (my_list is None or x < 0):
        return (0)

    try:
        while (i < x):
            print("{:d}".format(my_list[i]), end='')
            i += 1
    except ValueError:
        print()
        return (i)
    except TypeError:
        print()
        return (i)

    print()
    return (i)
