#!/usr/bin/python3
"""This module contans a load_from_json_file func"""
import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file"""

    with open(filename, encoding='utf-8') as f:
        return (json.load(f))
