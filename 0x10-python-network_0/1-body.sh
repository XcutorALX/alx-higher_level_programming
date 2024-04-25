#!/bin/bash
# This script displays the body of an http response if the error code is 200
[ "$(curl -sL -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -sL "$1"
