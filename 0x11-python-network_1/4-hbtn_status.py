#!/usr/bin/python3
"""
This python script fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    response = r.content.decode("utf-8")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
