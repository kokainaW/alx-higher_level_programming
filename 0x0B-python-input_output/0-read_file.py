#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as f:
        for li in f:
            print(li, end="")
    f.closed
