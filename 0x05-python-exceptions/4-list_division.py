#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    
    if (list_length <= 0):
        return ([])

    if (my_list_1 is None or my_list_2 is None):
        return ([i for i in range(list_length)])

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            newList.append(result)

    return (newList)
