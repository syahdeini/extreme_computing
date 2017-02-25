#!/usr/bin/python

import sys
import re
for line in sys.stdin:
    line = line.strip()
    z = re.split('[\s]\s*',line)
    print("{0}\t{1}\t{2}\t{3}".format(z[0],z[1],z[2],z[3]))

