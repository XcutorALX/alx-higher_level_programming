#!/usr/bin/python3
"""
This script uses urllib module to diplay the result of fetching a url
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {r.status_code}")
