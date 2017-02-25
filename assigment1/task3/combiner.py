#!/usr/bin/python

import sys

def get_max(a,b):
    if a > b:
        return a
    return b


max_sentence_len=0
max_token_len=0
for line in sys.stdin:
        line = line.strip()
        sentence_len, token_len = line.split("\t",1)
        sentence_len = int(sentence_len)
        token_len = int(token_len)
        max_sentence_len = get_max(sentence_len, max_sentence_len)
        max_token_len = get_max(token_len, max_token_len)

print("{0}\t{1}".format(max_sentence_len, max_token_len))
