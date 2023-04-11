#!/usr/bin/python3
"""
This module  takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

if __name__ == '__name__':
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        html = response.getheader('X-Request-Id')
        print(html)
