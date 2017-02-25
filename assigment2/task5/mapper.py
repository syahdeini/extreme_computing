#!/usr/bin/python

import sys
import os
import random

line_number = 0
for line in sys.stdin:
   if random.randint(0,line_number) == 0:
      reservoir = line.strip()
   line_number += 1
print("{0}\t{1}".format(line_number,reservoir))

