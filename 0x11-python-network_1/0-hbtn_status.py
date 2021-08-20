#!/usr/bin/python3
"""
a Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request as request

if __name__ == "__main__":

    with request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print('Body response:')
        print("\t- type: {}".format(html))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
