#!/usr/bin/bash
# Script that sends an http request and displays the length of the response
curl -s -w %{size_download}"\n" "$1" -o /dev/null
