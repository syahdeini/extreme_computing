#!/usr/bin/python

import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q

# mapper 2 sill try to combine file 
def print_dict(_dict):
  for key in _dict:
    print("{0}\t{1}\t{2}".format(key,len(_dict[key]),','.join(_dict[key])))

dict_user = {}

prev_answ_id = ""
prev_owner_id = -1
for line in sys.stdin:
   line = line.strip()
   answ_id,owner_id = line.split()
   if owner_id in dict_user:
      dict_user[owner_id].append(answ_id)
   else:
      dict_user[owner_id] = [answ_id]
   if(sys.getsizeof(dict_user) > 899 * 1024 * 1024):
      print_dict(dict_user)
      dict_user.clear()
print_dict(dict_user)
