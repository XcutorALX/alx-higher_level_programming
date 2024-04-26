#!/usr/bin/python3
"""
This script uses urllib module to diplay the result of fetching a url
"""
if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    data = {"email": argv[2]}
    data = urlencode(data).encode('utf-8')
    req = Request(argv[1], data=data, method="POST")
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
