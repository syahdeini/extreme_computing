#!/usr/bin/python

import sys
import re

def split_join(mark):
  mark = re.split('[\s]\s*',mark)
  mark = ",".join(mark)
  return mark

def total_average(total,counter):
    if counter > 3:
      return total/float(counter)
    else:
      return 0
    
prev_student_id = ""
all_total = 0
all_counter = 0
max_average = 0
max_student_name =[]
prev_student_name = "" 
for line in sys.stdin:
  line = line.strip()
  student_id,student_name,total,counter = re.split('[\s]\s*',line)
  if prev_student_id == student_id:
      all_counter += int(counter)
      all_total += int(total)
  else: # mark
     average = total_average(all_total, all_counter)
     if average > max_average:
        max_student_name=[prev_student_name]
        max_average = average
     elif average == max_average:
        max_student_name.append(prev_student_name)
     prev_student_id = student_id
     all_total = int(total)
     all_counter = int(counter)
     prev_student_name = student_name
print(" ".join(max_student_name))
