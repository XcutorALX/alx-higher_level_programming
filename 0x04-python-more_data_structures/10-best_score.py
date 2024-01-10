#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    maxScore = {'best': ['none', 0]}
    for key in a_dictionary:
        if a_dictionary[key] > maxScore['best'][1]:
            maxScore['best'] = [key, a_dictionary[key]]

    if maxScore['best'][1] == 0:
        return None

    return maxScore['best'][0]
