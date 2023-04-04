#!/usr/bin/env bash
# Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

url=$1

curl -sI -w ''%{size_header} "$url" | tail -1; echo ""
