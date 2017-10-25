# !/usr/local/bin/python3.4.2
# ----Copyright (c) 2016 Carnegie Hall | The MIT License (MIT)----
# ----For the full license terms, please visit https://github.com/CarnegieHall/quality-control/blob/master/LICENSE---- 
# Argument 0 is the script
# Argument 1 is the DAMS export of all Getty IDs in Cortex
# Argument 2 is the new Getty metadata CSV which contains all IDs that should be ingested
# Argument 3 is the word test # youre on

import csv
import os
import sys

filePath_1 = str(sys.argv[1])
filePath_2 = str(sys.argv[2])
volume = str(sys.argv[3])

fileCheckList = []
fileDict = {}

# print(os.path.split(filePath_2)[0])

with open(filePath_1, 'rU') as f:
    cortexFiles = csv.reader(f, dialect='excel', delimiter=',', quotechar='"')
    for row in cortexFiles:
    	filenameDAMS = row[1]
    	fileCheckList.append(filenameDAMS)

with open(filePath_2, 'rU') as k:
	assetStagingFiles = csv.reader(k, dialect='excel', delimiter=',', quotechar='"')
	next(assetStagingFiles)
	for row in assetStagingFiles:
		filenameAssetStaging = row[0]
		opasID = row[27]
# Check loop finds filenames missing from the DAMS list (but appearing in asset staging) and adds them to fileDict, which will be printed to create an updated central CSV.
		if opasID not in fileCheckList:
			fileDict[opasID] = opasID


matchedFiles_name = ''.join([str(os.path.split(filePath_2)[0]), '/GettyIDs_reconcile_', volume, '.csv'])

with open(matchedFiles_name, 'w', newline='') as thing:
	a = csv.writer(thing, dialect='excel', delimiter=',')
	a.writerow(["Program File Name", "OPAS ID for Cortex"])
	for key, value in fileDict.items():
		a.writerow([key, value])

print("Done with preparing new Central CSV for volume ", volume)
