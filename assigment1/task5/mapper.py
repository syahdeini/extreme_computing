#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    tokens, count = line.split("\t",1)
    print("{0}\t{1}".format(count, tokens))

