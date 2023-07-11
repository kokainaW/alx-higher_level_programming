#!/usr/bin/python3
"""Task 0"""
def read_file(filename=""):
    with open(filename, 'r') as f:
        for li in f:
            print(li, end="")
    f.closed
