#!/usr/bin/python3
"""
This script uses urllib module to diplay the result of fetching a url
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv

    urlopen = urllib.request.urlopen
    with urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
