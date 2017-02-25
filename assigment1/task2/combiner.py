#!/usr/bin/python

import sys

prev_line = ""
prev_flag = 1

for line in sys.stdin:
        line = line.strip()
        line, flag = line.split("\t", 1)
        flag = int(flag)
        if prev_line == line:
           prev_flag = 0
        else:
            if prev_line:
                    print("{0}\t{1}".format(prev_line,prev_flag))
            prev_flag=flag
            prev_line = line

if prev_line and prev_flag:     # print the last line
    print("{0}\t{1}".format(prev_line,flag))

