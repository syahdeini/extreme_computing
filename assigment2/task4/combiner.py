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

prev_answ_id = ""
prev_owner_id = -1
for line in sys.stdin:
   line = line.strip()
   answ_id,owner_id,status = line.split()
   #print(line)
   if status == '-1':
           if answ_id == prev_answ_id:  #found the ownerid
              if owner_id != '-1':
                  prev_owner_id = owner_id
              print("{0}\t{1}\t{2}".format(answ_id,prev_owner_id,1))
              prev_answ_id = ""
              prev_owner_id = -1
           else : # not found user id, print the previous line
               if prev_answ_id:
                   print("{0}\t{1}\t{2}".format(prev_answ_id,prev_owner_id,-1))
               prev_answ_id = answ_id
               if owner_id != '-1':
                    prev_owner_id = owner_id
   else: # already solved
           print("{0}\t{1}\t{2}".format(answ_id,owner_id,status))




if status == '-1' and prev_answ_id: # for the last line
   print("{0}\t{1}\t{2}".format(prev_answ_id,prev_owner_id,-1))

