#!/usr/bin/python

import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q
# assume that the mapper output will be sorted

dict_key = {}
# filename = "hahaha" # for testing purpose


def print_all_list(owner_id,total_count,post_list):
        post_list= ','.join(post_list)
        print("{0}\t{1}\t{2}".format(owner_id,total_count,post_list))

prev_answ_list = []
prev_owner_id = ""
prev_count = 0
for line in sys.stdin:
   line = line.strip()
   owner_id,count,ans_id_list = line.split()
   if prev_owner_id == owner_id:
      prev_count += len(ans_id_list.split(','))
      prev_answ_list += ','+ans_id_list 
   else: # different owner
      if prev_owner_id:
        print("{0}\t{1}\t{2}".format(prev_owner_id,prev_count,prev_answ_list))
      prev_owner_id = owner_id
      prev_answ_list = ans_id_list
      prev_count = int(count)
if prev_owner_id == owner_id:
    print("{0}\t{1}\t{2}".format(prev_owner_id,prev_count,prev_answ_list))

