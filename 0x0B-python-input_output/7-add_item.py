#!/usr/bin/python3
"""
This module works with the command line
"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


cmd_line = sys.argv
filename = 'add_item.json'
content = []
if filename in os.listdir():
    content = load_from_json_file(filename)
    content += cmd_line[1:]
    save_to_json_file(content, filename)
else:
    content += cmd_line[1:]
    save_to_json_file(content, filename)
