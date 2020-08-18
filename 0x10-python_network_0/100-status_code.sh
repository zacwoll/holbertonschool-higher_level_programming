#!/bin/bash
# Bash Script that sends a req to URL and displays the status code
curl -so /dev/null -w "%{http_code}" "$1"
