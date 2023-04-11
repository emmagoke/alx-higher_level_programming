#!/usr/bin/python3
import sys
import urllib.request


url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    html = response.getheader('X-Request-Id')
    print(html)
