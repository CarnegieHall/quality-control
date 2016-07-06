# !/usr/local/bin/python3.4.2
# ----Copyright (c) 2016 Carnegie Hall | The MIT License (MIT)----
# ----For the full license terms, please visit https://github.com/CarnegieHall/quality-control/blob/master/LICENSE----
# argument 0 is the script name
# argument 1 is the path to the grandparent directory of all assets
# argument 2 is the path to the metadata spreadsheet 
# argument 3 is the path to the target destination directory for subset of assets


import csv
import os
from os import listdir
from os.path import isfile, join, split
import sys
import shutil
from shutil import copyfile

# def copyFile(src, dest):
#     try:
#         shutil.copy(src, dest)
#     # eg. src and dest are the same file
#     except shutil.Error as e:
#         print('Error: %s' % e)
#     # eg. source or destination doesn't exist
#     except IOError as e:
#         print('Error: %s' % e.strerror)

#Set filepath variables
filePath_1 = str(sys.argv[1])
filePath_2 = str(sys.argv[2])
filePath_3 = str(sys.argv[3])

# for files in os.walk(filePath_1):
# 	print(files[2])


with open(filePath_2, 'rU') as f:
	fileData = csv.reader(f, dialect='excel', delimiter=',')
	next(fileData, None)  # skip the headers
	for row in fileData:
		#verify row #
		uploadFilename = row[17]
		# print(uploadFilename)
		for rootFolder, subdirFolder, files in os.walk(filePath_1):
			# matchedFile = files[2]
			var1 = rootFolder
			var2 = subdirFolder
			var3 = files
			# print(var1)
			# print(var2)
			# print(var3)
			for item in files:
				if uploadFilename in item:
					# print(uploadFilename, '\t', files)
					inputPath = ''.join([str(var1), '/', str(uploadFilename)])
					# print(inputPath)
		# shutil.copy(src, dst) does not preserve original modification and access datetime stamps. Benefits are this is faster than shutil.copy2
		if inputPath is None:
			print('File not found:', '\t', uploadFilename)
		else:
			shutil.copy2(inputPath, filePath_3)
			print('File copied:', '\t', uploadFilename)

