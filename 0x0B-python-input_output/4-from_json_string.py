#!/usr/bin/python3
"""This module contains a from_json_string func"""
import json


def from_json_string(my_string):
    """Returns the object representation of a json str"""
    return (json.loads(my_string))
