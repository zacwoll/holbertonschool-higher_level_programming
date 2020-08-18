#!/bin/bash
# Bash script that Takes URL, sends POST req, displays body of reponse
curl -sX POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
