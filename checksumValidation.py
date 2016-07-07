#!/usr/local/bin/python3.4
# ----Copyright (c) 2016 Carnegie Hall | The MIT License (MIT)----
# ----For the full license terms, please visit https://github.com/CarnegieHall/quality-control/blob/master/LICENSE----
# requires csv, json, sys, time
# input file structure is a CSV with md5 hash value, md5 creation date time stamp, filename, mime type, last modified date time stamp, path to the file
# run script with 5 arguments:
# argument 0 is the script name
# argument 1 is the path to the Harddrive checksums output
# argument 2 is the path to the Isilon checksums output
# argument 3 is the path to the checksum validation directory you want the TXT to be saved to
# argument 4 is the harddrive ID/volume that will be added to the output filename (E.g. 12-306)

import csv
import json
import sys
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
cmdargs = str(sys.argv)
hd_fileDict = {}
isilon_fileDict = {}
#matchString is just a long string, with tabs and newline characters that will be output as a .txt file
matchString = ''
volume = sys.argv[len(sys.argv)-1]
outputPath = sys.argv[len(sys.argv)-2]

with open(str(sys.argv[1]), 'rU') as f, open(str(sys.argv[2]), 'rU') as g:
    hardDrive = csv.reader(f, delimiter=',', quotechar='"')
    next(hardDrive, None)  # skip the headers
    isilon = csv.reader(g, delimiter=',', quotechar='"')
    next(isilon, None)  # skip the headers

    for row in hardDrive:
        hd_fileDict[str(row[2])] = row[0]
    for row in isilon:
        isilon_fileDict[str(row[2])] = row[0]

# #This print command will allow you to double-check the dictionaries by printing one (or both)
# print (json.dumps(hd_fileDict, indent=4))
        
#     #This loops through the hard drive files and sets a variable "checksum" for the checksum. This takes the MediaPreserve-created checksums which are all uppercase and makes them lowercase alphanumeric
        #strings so that they validate against the checksums we create locally.
    for key in hd_fileDict:
        checksum = hd_fileDict[str(key)].lower()

        #For each HD filename, this checks to see if that filename exists in the Isilon dictionary
        #If it is missing, it constructs a string to add to our output file
        #Else: file exist in both; see if the checksums match and write a string accordingly (PASS/FAIL) 
        if key not in isilon_fileDict:
            myString = str(key) + '\t' + checksum + '\t' + "MISSING" + '\n'
            matchString += myString
        else:      
            if checksum == isilon_fileDict[str(key)]:
                myString = str(key) + '\t' + checksum + '\t' + "PASS" + '\n'
                matchString += myString
            else:
                myString = str(key) + '\t' + checksum + '\t' + "FAIL" + '\n'
                matchString += myString
                
# # #This is just to check your results - it will print all of the filenames, checksums, and PASS/FAIL or MISSING
# print(matchString)


# #Saves the results as a text file with a datetimestamp in the output filename
outputFilename = ''.join('checksumValidation_' + volume + '_' + timestr)
outputFullPath = ''.join(outputPath + '/' + '%s.txt' % outputFilename)
newfile = open(outputFullPath, 'w')
header = str('HD Filename' + '\t' + 'HD Checksum' + '\t' + 'Status' + '\n')
newfile.write(header)
newfile.write(matchString)
newfile.close()