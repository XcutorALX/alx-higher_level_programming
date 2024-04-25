#!/bin/bash
# Script that sends an http request and displays the length of the response
curl -sI $1 | grep "Content-Length" | grep -oP "\d+"
