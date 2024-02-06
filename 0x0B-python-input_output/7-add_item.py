#!/usr/bin/python3
"""This module adds arguments to a list and saves as json"""
from sys import argv
import json
save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
with open(filename, encoding="utf-8", mode="w+") as f:
    my_list = []

    if f.read() != "":
        f.seek(0)
        my_list = json.load(f)

    my_list += argv[1:]
    json.dump(my_list, f)
