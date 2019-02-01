# !/usr/local/bin/python3.4.3
# ----Copyright (c) 2019 Carnegie Hall | The MIT License (MIT)----
# run script with 4 arguments:
# argument 0 is the script name
# argument 1 is path to List1: SHORTER list CSV (contains only some items)
# argument 2 is path to List2: LONGER list CSV (contains all items)
# argument 3 is directory you want to save output CSV to (that lists all items in List2 that are NOT in List1)

import csv
import os
from os.path import join
import sys

filePath1 = str(sys.argv[1])
filePath2 = str(sys.argv[2])
filePath3 = str(sys.argv[3])

itemSubtypes = []
unmatchedIDs = []
allSubtypes = []

with open(filePath1, 'rU') as f1:
    itemData 1 = csv.reader(f1, dialect='excel', delimiter=',', quotechar='"')
    next(itemData 1, None)  # skip the headers
    for row in itemData 1:
    	itemID = row[0]
    	itemSubtypes.append(itemID)

with open(filePath2, 'rU') as f2:
    itemData 2 = csv.reader(f2, dialect='excel', delimiter=',', quotechar='"')
    next(itemData 2, None)  # skip the headers
    for row in itemData 2:
    	itemID = row[0]
    	allSubtypes.append(itemID)

for item in allSubtypes:
	if item not in itemSubtypes:
		unmatchedIDs.append(item)

outputPath = ''.join([str(filePath3), '/umatchedIDs.csv'])

#maybe write out as a string? and open it up in excel as a workaround? what is wrong below?
# would have to import data from text in excel with this:
#This saves the unmatched OPAS IDs as a text file, so you can check the issues in OPAS
# with open(unmatchedIDs_name, 'w') as h:
#     h.write(','.join(str(opas_id) for opas_id in unmatchedIDs))


with open(outputPath, 'a') as h:
	h = csv.writer(h, dialect='excel', quotechar='"', quoting=csv.QUOTE_ALL)
	h.writerow(unmatchedIDs)

print('Done!')