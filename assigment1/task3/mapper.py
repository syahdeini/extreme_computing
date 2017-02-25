#!/usr/bin/python

import sys

def find_max_token(line):
       len_max = 0
       for token in line.split():
            len_token = len(token)
            if len(token) > len_max:
                    len_max= len(token)
       return len_max
for line in sys.stdin:
    line = line.strip()
    print("{0}\t{1}".format(len(line),find_max_token(line)))
