#!/usr/bin/python

import sys


pred_token = ""
token = ""
count_value = 0
token_dict = {}
for line in sys.stdin:
  line = line.strip()
  token, value = line.split("\t", 1)
  value = int(value)
  if pred_token == token:
     count_value+=value
  else:
     if pred_token:
        print("{0}\t{1}".format(pred_token, count_value))
     pred_token = token
     count_value = value

if pred_token == token:
     print("{0}\t{1}".format(pred_token, count_value))
