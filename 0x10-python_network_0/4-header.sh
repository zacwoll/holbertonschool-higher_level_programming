#!/bin/bash
# Bash Script that takes in URL, sends GET req, displays body, uses Header
curl -sL "$1" -H "X-HolbertonSchool-User-Id: 98"
