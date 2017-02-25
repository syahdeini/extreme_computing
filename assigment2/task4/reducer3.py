#!/usr/bin/python

import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q
# 1 reducer

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


splited_list = max_answ_id_list.split(',')
splited_list = sorted(splited_list, key=lambda x: int(x))
print("{0}\t-> {1},\t{2}".format(max_owner_id,max_count,','.join(splited_list)))



