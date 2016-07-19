#!/usr/bin/env python

import sys
from sys import exit

current_count = 0
current_combo = None
#word = None
combo = None

# input comes from STDIN
for line in sys.stdin:

	# remove leading and trailing whitespace
	line = line.strip()
	try:
		dept, year, sales = line.split('\t',2)
	except ValueError:
		continue

	try:
		sales = float(sales)
	except ValueError:
		continue

	combo = dept + ' ' + year
	if current_combo == combo:
		current_count += sales
	else:
		if current_combo:
			if current_count > 25000000:
				deptnum, years = current_combo.split()
				print('%s\t%s\t%s' %(deptnum, years, current_count))
		current_count = sales
		current_combo = combo
	
if current_count > 25000000:
	print('%s\t%s\t%s' %(dept,year,sales))
