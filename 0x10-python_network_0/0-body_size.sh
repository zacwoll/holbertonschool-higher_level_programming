#!/bin/bash
# Takes in a URL, requests that url and displays the size of the body of the response
curl -sI "$1" | grep "Content-Length: " | awk '{print $2}'
