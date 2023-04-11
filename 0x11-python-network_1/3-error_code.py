#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8)."""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = request.Request(url)
        with request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
