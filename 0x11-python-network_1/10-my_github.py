#!/usr/bin/python3
"""
This script uses urllib module to diplay the result of fetching a url
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(argv[1], argv[2]))
    r_json = r.json()
    if r_json == {}:
        print("None")
    else:
        print("{}".format(r_json.get('id')))
