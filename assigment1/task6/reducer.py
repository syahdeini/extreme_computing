#!/usr/bin/python

import sys
from math import log
from collections import OrderedDict

def calculate_entropy_list(key,value_list):
            total_value = sum(value_list)
            single_ent = 0
            for value in value_list:
                    prob=value/float(total_value)
                    single_ent = single_ent + (-1*prob*log(prob,2))
            print("{0} {1}".format(key,single_ent))


cond_dict={}
prev_condition = ""
count_list=[]
count_value = 0
for line in sys.stdin:
  line = line.strip()
  token, value = line.rsplit(" ", 1)
  value = int(value)
  cond, given_cond = token.rsplit(" ",1)
  if prev_condition == cond:
        count_list.append(value)
  else: # new condition
        if cond:
            if prev_condition: # to avoid first
                # calculate_entropy_list(prev_condition,count_list)
                
            prev_condition = cond
            del count_list[:]
            count_list=[value]

calculate_entropy_list(prev_condition, count_list)

