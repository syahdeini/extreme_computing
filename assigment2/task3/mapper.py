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
      if row.attrib["PostTypeId"] == '2': # question
        owner_id = int(row.attrib["OwnerUserId"])
        post_id = row.attrib["Id"]
        print("{0}\t{1}\t{2}".format(owner_id,1,post_id))
