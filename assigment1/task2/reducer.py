#!/usr/bin/python

import sys

prev_sentence= ""
pred_flag = None
for line in sys.stdin:
        line = line.strip()
        sentence, next_flag = line.split("\t",1)
        if pred_flag is None:
            pred_flag = int(next_flag)
        if prev_sentence == sentence:
            pred_flag = 0
        else:
            if prev_sentence and (pred_flag > 0):
                print("{0}".format(prev_sentence))
            pred_flag = int(next_flag)
            prev_sentence = sentence
if prev_sentence and (pred_flag>0):
        print("{0}".format(prev_sentence))
