#!/usr/bin/python

import sys


lines_set = set()


def print_set():
	for i in lines_set:
		print i
	dlines_set.clear()
	d
def check_memory_bound():
	if sys.getsizeof(lines_set)> 1024*1024*1024*1024: # if the set more than 1 gigabyte
		print_set()
		
	
def add_to_set(line):
	lines_set.add(line)
	check_memory_bound()

for line in sys.stdin:
    line = line.strip()
    token_list=line.split()
    for pointer in range(len(token_list)-2):
        token=" ".join(token_list[pointer:3+pointer])
        print("{0}\t{1}".format(token,1))
