#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
	#line = line.strip()
	store, dept, date, sales = line.split('\t', 3)
	print('%s\t%s\t%s' % (dept, date[:4], sales))