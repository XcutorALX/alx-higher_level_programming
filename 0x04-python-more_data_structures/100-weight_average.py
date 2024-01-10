#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_average = 0
    divisor = 0

    for item in my_list:
        weighted_average += (item[0] * item[1])
        divisor += item[1]

    if divisor == 0 or weighted_average == 0:
        return 0

    return weighted_average / divisor
