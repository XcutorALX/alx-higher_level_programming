#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """This function prints prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: the text to print
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    text = text.strip()

    start = 0
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print(text[start:i].strip() + text[i] + '\n')
            start = i + 1

    if start != len(text):
        print(text[start:len(text)].strip())
