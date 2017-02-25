#!/usr/bin/python

import sys
import os
import random
import re

def print_dict(_dict_key,_filename):
    m = re.search('([1-9][0-9]*)',_filename) # getting the filename number
    num_of_file = 0 #default number of file
    if m: # if availible
        num_of_file = m.group(0)
    for key in _dict_key:
           print("{0} {1} {2} {3}".format(key,num_of_file,_filename,_dict_key[key]))


dict_key = {}
 # for testing purpose
#filename = str(random.randint(1,100))
filename = os.environ["mapreduce_map_input_file"].split('/')[-1]

for line in sys.stdin:
   line = line.strip()
   line = line.split()
   for word in line:
           if word in dict_key:
                dict_key[word]+=1
           else:
                dict_key[word]=1
           if(sys.getsizeof(dict_key) >=  899*1024*1024): #bounded memory 800MB
                print_dict(dict_key,filename)
                dict_key.clear()

print_dict(dict_key,filename)

