#!/bin/bash
# This bash script  sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -X DELETE -sL "$1"
