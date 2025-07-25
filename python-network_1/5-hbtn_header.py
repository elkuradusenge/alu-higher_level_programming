#!/usr/bin/python3
"""
Script that takes in URL parameter, send in request and
prints X-Request-Id from the response.
"""
import requests
import sys

if __name__ == '__main__':

    res = requests.get(sys.argv[1])
    head = res.headers.get('X-Request-Id')
    print(head)
