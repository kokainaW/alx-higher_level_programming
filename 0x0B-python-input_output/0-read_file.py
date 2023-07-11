#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as z:
        for li in z:
            print(li, end="")
    z.closed
