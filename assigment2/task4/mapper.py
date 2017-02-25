#!/usr/bin/python

import sys
import os
import xml.etree.ElementTree as ET
import Queue as Q


dict_key = {}
# filename = "hahaha" # for testing purpose

for line in sys.stdin:
   line = line.strip()
   # line = line.split()
   root = ET.fromstring(line)
   for row in root.iter("row"):
      if row.attrib["PostTypeId"] == '1': # question
       # try:
        if "AcceptedAnswerId" in row.attrib:
            accepted_answ_id = row.attrib["AcceptedAnswerId"]
            print("{0}\t{1}\t{2}".format(accepted_answ_id,-1,-1))
      elif row.attrib["PostTypeId"] == '2':
        answ_id =  row.attrib["Id"]
        owner_id = row.attrib["OwnerUserId"]
        print("{0}\t{1}\t{2}".format(answ_id,owner_id,-1))
