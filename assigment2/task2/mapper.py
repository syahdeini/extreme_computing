#!/usr/bin/python
# can't do priority queue here because there will be a post with diffrenet id in other place
import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q


# dict_key = {}
# filename = "hahaha" # for testing purpose

# q = Q.PriorityQueue()
# def add_to_pque(key, id_val):
#   q.put((-1*key, id_val))
#   if q.qsize() > 20:
#     q.get()

for line in sys.stdin:
   line = line.strip()
   # line = line.split()
   root = ET.fromstring(line)
   for row in root.iter("row"):
      if row.attrib["PostTypeId"] == '1': # question
        value = int(row.attrib["ViewCount"])
        _id = row.attrib["Id"]
        print("{0}\t{1}".format(_id,value))

        # add_to_pque(value,_id)

# for i in range(20):
#     count, id_val = q.get()
#     count = count*-1
