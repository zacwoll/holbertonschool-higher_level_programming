#!/bin/bash
# Write a script that makes a req to 0.0.0.0:5000/catch_me that responds with You got me!
curl -sLX PUT -d 'user_id=98' -H 'Origin: HolbertonSchool' 0.0.0.0:5000/catch_me
