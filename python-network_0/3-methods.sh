#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods that are accepted by the server.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
