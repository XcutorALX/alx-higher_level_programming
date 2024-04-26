#!/usr/bin/python3
"""
This script uses urllib module to diplay the result of fetching a url
"""
if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    message = r.text
    print("Body response:")
    print(f"\t- type: {type(message)}")
    print(f"\t- content: {message}")
