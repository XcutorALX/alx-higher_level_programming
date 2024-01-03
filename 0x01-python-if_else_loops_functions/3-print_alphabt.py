#!/usr/bin/python3
for char in range(97, 123):
    if not (chr(char) == 'q' or chr(char) == 'e'):
        print("{}".format(chr(char)), end="")
