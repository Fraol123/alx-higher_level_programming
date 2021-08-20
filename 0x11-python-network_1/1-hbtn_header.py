#!/usr/bin/python3
"""
Displays the X-request-Id header variable of a request to a given URL
Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
