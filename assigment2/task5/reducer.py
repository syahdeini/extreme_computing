#!/usr/bin/python

import sys
import os
import random



prev_line_num, reservoir = sys.stdin.readline().strip().split("\t")
prev_line_num = int(prev_line_num)
for line in sys.stdin:
   line = line.strip()
   line_num,sentence = line.split("\t")
   line_num = int(line_num)
   if random.randint(0,line_num+prev_line_num) <= prev_line_num:
      reservoir = sentence
   prev_line_num += line_num
print(reservoir)

