#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    z = re.split('[\s]\s*',line,maxsplit=2)
    print("{0}\t{1}\t{2}".format(z[1], z[0], z[2]))

