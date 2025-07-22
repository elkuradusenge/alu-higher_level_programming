#!/bin/bash
# Bash script that takes in a URL as parameter sends a GET request and prints response
curl -sH "X-School-User-Id: 98" "$1"
