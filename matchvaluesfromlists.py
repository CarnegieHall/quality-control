# !/usr/local/bin/python3.4.2
# ----Copyright (c) 2017 Carnegie Hall | The MIT License (MIT)----
# ----For the full license terms, please visit https://github.com/CarnegieHall/quality-control/blob/master/LICENSE----
# run script with 3 or more arguments:
# argument 0 is the script name
# argument 1 is the path to the database IDs and filenames
# argument 2 is the path to the database IDs and asset IDs
# argument 3 is the path you want to output the matched CSV to
# argument 4 is the Batch ID of the subset of photographs (e.g. GB-006)


import csv
import os
from os.path import isfile, join, split
import sys
import io

#Set filepath variables
filePath_1 = str(sys.argv[1])
filePath_2 = str(sys.argv[2])
filePath_3 = str(sys.argv[3])
batch = str(sys.argv[4])

filenameDict = {}
assetidDict = {}
simplifiedDict = {}

with open(filePath_1, 'rU') as f, open(filePath_2, 'rU') as g:
	filenameData = csv.reader(f, dialect='excel', delimiter=',')
	next(filenameData, None)  # skip the headers
	assetData = csv.reader(g,dialect='excel', delimiter=',')
	for row in assetData:
		database_id = row[0]
		asset_id = row[1]
		assetidDict[database_id] = asset_id 

	for row in filenameData:
		database_id_2 = row[0]
		uploadfilename = row[1]
		asset_id = assetidDict[database_id_2]

		simplifiedDict[asset_id] = uploadfilename


outputPath = ''.join([str(filePath_3), '/SimplifiedMatching', batch, '.csv'])

with open(outputPath, 'w', newline='') as csvfile:
	w = csv.writer(csvfile, dialect='excel', delimiter=',')
	for k,v in simplifiedDict.items():
		w.writerow([k,v])