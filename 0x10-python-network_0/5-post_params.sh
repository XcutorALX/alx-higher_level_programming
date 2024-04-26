#!/bin/bash
# A script that sends GET request with additional info
curl -s -X "POST" "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
