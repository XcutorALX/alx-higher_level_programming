#!/usr/bin/python3
"""
This script uses urllib module to diplay the result of fetching a url
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    data = {"email": argv[2]}
    r = requests.post(argv[1], data=data)
    print(r.text)
