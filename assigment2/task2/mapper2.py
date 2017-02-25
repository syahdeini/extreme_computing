#!/usr/bin/python
# can't do priority queue here because there will be a post with diffrenet id in other place
import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q



def print_queue(_q):
    for i in range(20):
        count, id_val = _q.get()
        count = count*-1
        print("{0}\t{1}".format(id_val,count))
    return _q


def add_to_pque(_q,key, id_val):
  _q.put((-1*key, id_val))
  if sys.getsizeof(_q) >= 899*1024*1024:
    _q=print_queue(_q) 
  return _q

q = Q.PriorityQueue()
for line in sys.stdin:
   line = line.strip()
   _id,value = line.split()
   #print("{0}\t{1}".format(_id,value))
   value = int(value)
   q=add_to_pque(q,value,_id)
print_queue(q)
