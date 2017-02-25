#!/usr/bin/python


import sys

def print_mark(student_name, student_id, counter, total):
    print("{0}\t{1}\t{2}\t{3}".format(student_id,student_name,total,counter))


mark_list=[]
prev_stud_id = ""
pred_token = ""
student_name = ""
total = 0
counter=0
for line in sys.stdin:
  line = line.strip()
  stud_id,key,value = line.split("\t",2)
  if key=="student":
      if counter!=0 and student_name :
        print_mark( student_name, prev_stud_id, counter, total )
      prev_stud_id = stud_id
      counter = 0
      total = 0
      student_name = value
  elif key=="mark": # mark
      _,val = value.split()
      total += int(val)
      counter +=1

if counter!=0 and student_name:
        print_mark( student_name, prev_stud_id, counter, total )

