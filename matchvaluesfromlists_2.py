# !/usr/local/bin/python3.4.2
# ----Copyright (c) 2017 Carnegie Hall | The MIT License (MIT)----
# ----For the full license terms, please visit https://github.com/CarnegieHall/quality-control/blob/master/LICENSE----
# run script with 3 or more arguments:
# argument 0 is the script name
# argument 1 is the path to the Legacy IDs and Upload Dates
# argument 2 is the path to the Asset IDs and Legacy IDs
# argument 3 is the path you want to output the matched CSV to
# argument 4 is a term to add to the output filename for disambiguation

import csv
import os
from os.path import isfile, join, split
import sys
import io

filePath_1 = str(sys.argv[1])
filePath_2 = str(sys.argv[2])
filePath_3 = str(sys.argv[3])
batch = str(sys.argv[4])

dateDict = {}
legacyIdDict = {}
simplifiedDict = {}


with open(filePath_1, 'rU') as f, open(filePath_2, 'rU') as g:
	dateData = csv.reader(f, dialect='excel', delimiter=',')
	next(dateData, None)  # skip the headers
	idData = csv.reader(g,dialect='excel', delimiter=',')
	for row in idData:
		dams_id = row[0]
		legacy_id = row[1]
		legacyIdDict[legacy_id] = dams_id

	for row in dateData:
		legacy_id_2 = row[0]
		uploadDate = row[1]
		if legacy_id_2 not in legacyIdDict:
			print('Not in DAMS: ',legacy_id_2)
		else:
			legacy_id = legacyIdDict[legacy_id_2]

			simplifiedDict[legacy_id] = uploadDate

outputPath = ''.join([str(filePath_3), '/UploadDates', batch, '.csv'])

with open(outputPath, 'w', newline='') as csvfile:
	w = csv.writer(csvfile, dialect='excel', delimiter=',')
	w.writerow(["DAMS ID", "Digital Accession Date"])
	for k,v in simplifiedDict.items():
		w.writerow([k,v])
		#need date value to be formatted as YYYY-MM-DD
