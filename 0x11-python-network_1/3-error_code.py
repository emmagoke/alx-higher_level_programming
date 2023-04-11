#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8)."""
import sys
import urllib

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
