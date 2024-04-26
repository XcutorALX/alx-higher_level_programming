#!/usr/bin/python3
"""
This script uses urllib module to diplay the result of fetching a url
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    message = ""
    if len(argv) > 1:
        message = argv[1]
    data = {"q": message}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        reply = r.json()
        if len(reply) != 0:
            print(f"[{reply.get('id')}] {reply.get('name')}")
        else:
            r.status_code = 204
            raise (ValueError)
    except ValueError as e:
        if r.status_code == 204:
            print("No result")
        else:
            print("Not a valid JSON")
