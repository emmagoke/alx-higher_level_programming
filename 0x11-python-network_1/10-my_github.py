#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__name__':
    username = sys.argv[1]
    password = sys.argv[2]  # The password is github access token
    auth = HTTPBasicAuth(username, password)
    response = requests.get('https://api.github.com/user', auth=auth)
    json = response.json()
    print(json.get('id'))
