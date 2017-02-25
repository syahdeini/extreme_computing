#!/usr/bin/python
# can't do priority queue here because there will be a post with diffrenet id in other place
import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q


dict_key = {}
# filename = "hahaha" # for testing purpose
i=0
for line in sys.stdin:
   line = line.strip()
   _id,value = line.split("\t")
   i+=1
   if i<=20:
        print("{0}\t{1}".format(_id,value))

