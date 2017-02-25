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

max_owner_id = ""
max_count = -1
max_answ_id_list = ""
for line in sys.stdin:
   line = line.strip()
   owner_id,count,ans_id_list = line.split()
   count = int(count)
   if count > max_count:
      max_count = count
      max_owner_id = owner_id
      max_answ_id_list = ans_id_list

print("{0}\t{1}\t{2}".format(max_owner_id,max_count,max_answ_id_list))

