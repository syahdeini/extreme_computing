#!/usr/bin/python

import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q


dict_key = {}
# filename = "hahaha" # for testing purpose


owner_id =""
max_owner =""
max_post_list=""
max_total_count =0
for line in sys.stdin:
   line = line.strip()
   owner_id,count,post_id = line.split("\t")
   count = int(count)
   if max_total_count < count:
     max_total_count = count
     max_owner = owner_id
     max_post_list = post_id

sort_post_id = max_post_list.split(",")
sort_post_id.sort()
sort_post_id = ','.join(sort_post_id)
print("{0}\t-> {1}".format(max_owner,sort_post_id))
