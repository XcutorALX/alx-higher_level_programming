#!/bin/bash
# this script displays the request types a server can handle
curl -sI "$1" | grep Allow | cut -d " " -f 2-
