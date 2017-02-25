#!/usr/bin/python

import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q


dict_key = {}
# filename = "hahaha" # for testing purpose


def print_all_list(owner_id,total_count,post_list):
        post_list= ','.join(post_list)
        print("{0}\t{1}\t{2}".format(owner_id,total_count,post_list))

owner_id =""
prev_owner =""
post_list=[]
total_count =0
for line in sys.stdin:
   line = line.strip()
   owner_id,count,post_id = line.split("\t")

   if prev_owner == owner_id:
     total_count+=int(count)
     post_list.append(post_id)
     if sys.getsizeof(post_list) > 899*1024*1024:
             print_all_list(prev_owner,total_count,post_list)
             # reset
             prev_owner =""
             post_list = []
             total_count = 0
   else:
     if prev_owner:
        print_all_list(prev_owner,total_count,post_list)
     prev_owner = owner_id
     total_count=int(count)
     post_list=[post_id]

if prev_owner == owner_id:
        print_all_list(prev_owner,total_count,post_list)
