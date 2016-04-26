# !/usr/local/bin/python3.4.2
# ----Copyright (c) 2016 Carnegie Hall | The MIT License (MIT)----
# ----For the full license terms, please visit https://github.com/CarnegieHall/quality-control/blob/master/LICENSE---- 
# This script scrapes md5 values from sidecar files provided by a digitization vendor
# requires csv, json, sys, time
# input file structure is a CSV with md5 hash value, md5 creation date time stamp, filename, mime type, last modified date time stamp, path to the file
# this script requires 4 arguments:
# argument 0 is the script name
# argument 1 is the path to the directory containing MD5 files
# argument 2 is the path to the checksums file output
# argument 3 is the harddrive ID/volume that will be added to the output filename (E.g. 12-306)

import csv
import fileinput
import glob
import io
import json
import os
import os.path
import sys
import time
from os import listdir
from os.path import isfile, join, split

timestr = time.strftime("%Y-%m-%dT%H:%M:%S")
filePath_1 = str(sys.argv[1])
filePath_2 = str(sys.argv[2])
volume = sys.argv[len(sys.argv)-1]
outputPath = filePath_2 + '/Vendor_Supplied_Checksums'
os.mkdir(outputPath)


checkSum_dict = {} 

for filename in glob.glob(os.path.join(filePath_1, '*.md5')):
    with open(filename, 'r') as f:
        text = f.read()
        checkSum = text.split('*')[0].strip()
        wavFile = text.split('*')[1].replace("\n", "")

        checkSum_dict[str(wavFile)] = {}
        checkSum_dict[str(wavFile)]['md5'] = checkSum
        checkSum_dict[str(wavFile)]['md5_datetime'] = timestr
        checkSum_dict[str(wavFile)]['filename'] = wavFile


checkSum_validationFile_name = ''.join([outputPath, '/Vendor_Supplied_Checksums', '_', volume, '.csv'])


fields = ['md5', 'md5_datetime', 'filename']
with open(checkSum_validationFile_name, 'w', newline='') as csvfile:
    w = csv.DictWriter(csvfile, fields)
    w.writeheader()
    for k in checkSum_dict:
        w.writerow({field: checkSum_dict[k].get(field) for field in fields})