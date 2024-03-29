#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': letter})
    try:
        json = response.json()
        if json:
            print(f"[{json.get('id')}] {json.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
