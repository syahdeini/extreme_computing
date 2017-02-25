#!/usr/bin/python

import sys
import re

def split_join(mark):
  mark = re.split('[\s]\s*',mark)
  mark = ",".join(mark)
  return mark

def print_mark_list(mark_list):
    mark_list = mark_list.split("~")
    for mark in mark_list[:-1]:
      mark = split_join(mark)
      print "("+mark+") ",
    mark = split_join(mark_list[-1])
    if mark:
      print("({0})".format(mark))
    else:
      print("")

mark_list=None
for line in sys.stdin:
  line = line.strip()
  stud_id,key,value = line.split("\t",2)
  if key == "student":
      if mark_list is not None :
        print_mark_list(mark_list)
      mark_list=""
      print value+" -->",
  else: # mark
      if len(mark_list)>0:
        mark_list+= ('~'+value)
      else:
        mark_list=value

