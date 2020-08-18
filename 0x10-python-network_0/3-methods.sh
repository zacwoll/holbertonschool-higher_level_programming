#!/bin/bash
# Write a bash script that takes in a URL and displays all HTTP methods allowed
curl -sI "$1" | awk '/Allow/' | cut -d" " -f2-
