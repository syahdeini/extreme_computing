#!/usr/bin/python

import sys
from collections import OrderedDict
N = 20

topN_dict={}
pred_token = ""
count_value = 0
for line in sys.stdin:
  line = line.strip()
  value, token = line.split("\t", 1)
  count_value+=1
  if count_value <= 20:
    print ("{0}\t{1}".format(value,token))
