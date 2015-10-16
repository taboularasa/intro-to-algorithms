#!/usr/local/bin/python

import sys

def rec_russian(a, b):
    if a == 0: return 0
    if a % 2 == 0: return 2 * rec_russian(a / 2, b)
    return b + 2 * rec_russian((a - 1) / 2, b)

if __name__ == "__main__":
    print rec_russian(int(sys.argv[1]), int(sys.argv[2]))
