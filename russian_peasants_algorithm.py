#!/usr/local/bin/python

import sys

def russian(a, b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    return z

if __name__ == "__main__":
    print russian(int(sys.argv[1]), int(sys.argv[2]))
