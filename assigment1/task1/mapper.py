#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    print("{0}".format(line.upper()))
