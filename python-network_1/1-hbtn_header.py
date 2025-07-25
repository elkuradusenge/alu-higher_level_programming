#!/usr/bin/python3
"""
Script that takes in URL parameter, send in request and
prints X-Request-Id from the response.
"""
import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        value = response.info()
    print(value['X-Request-Id'])
