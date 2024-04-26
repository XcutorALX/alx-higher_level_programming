#!/bin/bash
# This script posts the content of a file to a server with a POST request
curl -s -X POST $1 -H 'Content-Type: application/json' -d @$2
