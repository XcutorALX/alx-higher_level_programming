#!/usr/bin/python3
# This script uses urllib module to diplay the result of fetching a url
from urllib.request import urlopen


with urlopen("https://alx-intranet.hbtn.io/status") as response:
    message = response.read()
    print("Body response:")
    print(f"    - type: {type(message)}")
    print(f"    - content: {message}")
    print(f"    - typeutf8 content: {message.decode('utf-8')}")
