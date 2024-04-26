#!/usr/bin/python3
"""
This script uses urllib module to diplay the result of fetching a url
"""
if __name__ == "__main__":
    import urllib.request

    urlopen = urllib.request.urlopen
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        message = response.read()
        print("Body response:")
        print(f"\t- type: {type(message)}")
        print(f"\t- content: {message}")
        print(f"\t- utf8 content: {message.decode('utf-8')}")
