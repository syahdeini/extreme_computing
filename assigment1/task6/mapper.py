#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    seqtoken, value=line.split("\t")
    print("{0} {1}".format(seqtoken,value))

