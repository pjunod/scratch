#!/usr/bin/env python3

import logging
import random
import sys
quote = ""

''''
Python clone of unix cli app fortune
Input: ./.fortunes file containing quotes delineated by % on line before and after
	   Optional [int] argument to specify line to pull quote from
Output: Quote from line specified, or from random line if not specified
'''

logging.basicConfig(level=logging.INFO)

if len(sys.argv) > 1:
	start = int(sys.argv[1])
else: 
	start = None


try:
	# Read file in
	with open('.fortunes', 'r', encoding='utf-8') as flist:
		fortunes = flist.readlines()
except FileNotFoundError:
	logging.critical("Error: .fortunes file not found. Exiting....")
	sys.exit(1)

numlines = len(fortunes)
logging.debug("number of lines in .fortunes file: [%s]", numlines)
idxEnd = numlines - 1
logging.debug("index runs from 0 to [%s]", idxEnd)

# Make sure we're not specifying a line longer than the input file
if start is not None and numlines <= start:
	logging.error("line specification greather than length of quotes list")
	sys.exit(1)

if start is None:
	# Pick random line to start at
	# this is an index, so starts at 0 instead of 1
	start = random.randrange(0, numlines - 1)

logging.debug("Starting eval at index [%s]", start)

line = fortunes[start]
logging.debug("Line at initial eval is: [%s]", line.strip())
while line.strip() != '%' or start == numlines - 1:
	# wrap around if we hit the end of the file
	if start == numlines - 1:
		start = 0
		logging.debug("Wrap around end to beginning")
	else:
		start += 1
		logging.debug("Moved to index position [%s]", start)
	line = fortunes[start]

logging.debug("Found '%s' at index position [%s]", '%', start)
# Now we have the start of a line, get quote between next '%'
start += 1
line = fortunes[start]
logging.debug("Grabbing quote starting from index %s:[%s]]", start,line.strip())

while line.strip() != '%' and start <= idxEnd:
	quote += line
	logging.debug("quote so far: %s", quote)
	start += 1
	logging.debug("start is now [%s]", start)
	line = fortunes[start]
	logging.debug("next line is [%s]", line.strip())

quote = quote.strip()
logging.debug("Full quote: %s", quote)
print("############")
print(quote)
print("############")