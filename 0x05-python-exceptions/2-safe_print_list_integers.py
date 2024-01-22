#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0

    if (my_list is None or x < 0):
        return (0)

    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            pass
        except IndexError:
            print()
            return (i)
        i += 1

    print()
    return (i)
