#!/usr/bin/python3
# This script uses urllib module to diplay the result of fetching a url
from urllib.request import urlopen


with urlopen("http://unchaineddevs.tech") as response:
    message = response.read()
    print("Body response:")
    print(f"\t- type: {type(message)}")
    print(f"\t- content: {message}")
    print(f"\t- typeutf8 content: {message.decode('utf-8')}", end='')
