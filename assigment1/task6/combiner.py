#!/usr/bin/python

import sys
from collections import OrderedDict

pred_token = ""
count_value = 0
for line in sys.stdin:
  line = line.strip()
  value, token = line.split("\t", 1)
  value = int(value)
  if pred_token == token:
     count_value += value
  else:
     if pred_token:
        print("{0}\t{1}".format(count_value, pred_token))
     pred_token = token
     count_value = value


