#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    email = urllib.parse.urlencode({"email": email})
    email = email.encode('ascii')
    request = urllib.request.Request(url, email)
    with urllib.request.urlopen(request) as res:
        mail = res.read()
        print("{}".format(mail.decode('utf-8')))
