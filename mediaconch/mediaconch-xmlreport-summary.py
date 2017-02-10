#!/usr/local/bin/python3.4
# ----Copyright (c) 2016 Carnegie Hall | The MIT License (MIT)----
# ----For the full license terms, please visit https://github.com/CarnegieHall/quality-control/blob/master/LICENSE----
# argument 1 is the XML report

import sys

report = sys.argv[1]

import xml.etree.ElementTree as ET
tree = ET.parse(report)
root = tree.getroot()
cPass = 0
cFail = 0

for child in root:
	for grandchild in child:
		if grandchild.attrib['outcome'] == 'pass':
			cPass += 1
		if grandchild.attrib['outcome'] == 'fail':
			cFail += 1

print("Pass count: ",cPass,'\t',"Fail count: ",cFail)