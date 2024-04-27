#!/usr/bin/python3
"""
This scripts lists the 10 most recent commits of a repository
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
            }

    r = requests.get(url, headers=headers)
    try:
        message = r.json()
    except ValueError:
        message = dict()

    for key in message[:10]:
        print(f"{key['sha']}: {key['commit']['author']['name']}")
