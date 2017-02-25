#!/usr/bin/python


import sys

def print_mark(stud_id,mark_list):
        print("mark\t{0}\t{1}".format(stud_id,'~'.join(mark_list)))


mark_list=[]
prev_stud_id = ""
pred_token = ""
count_value = 0
for line in sys.stdin:
  line = line.strip()
  stud_id,key,value = line.split("\t",2)
  if key=="student":
      if mark_list:
        print_mark(prev_stud_id,mark_list)
      prev_stud_id = stud_id
      mark_list=[]
      print("student\t{0}\t{1}".format(stud_id,value))
  else:
      mark_list.append(value)
