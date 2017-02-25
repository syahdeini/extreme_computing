#!/usr/bin/python
'''
 Act like a combiner, just merging id and count
'''
import sys
import os


i=1
_id = 0
prev_id=""
count_total=0
for line in sys.stdin:
   line = line.strip()
   _id, count = line.split("\t")
   count = int(count)
   if prev_id == _id:
      count_total += count
   else:
        if prev_id:
          print("{0}\t{1}".format(_id,count))
        prev_id = _id
        count_total = count
if prev_id == _id:
    print("{0}\t{1}".format(_id,count))
