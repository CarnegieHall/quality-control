
#tech-notes

##USE CASES

Below are brief descriptions and snippets of code used to satisfy various small-scale use cases in our [quality control workflow](https://github.com/CarnegieHall/quality-control/blob/master/qc-workflow-overview.md). If you'd like to share your strategy for meeting any of the needs described below, please add a comment as a [new Issue](https://github.com/CarnegieHall/quality-control/issues). Feedback welcome.

###COPY/MOVE FILES
**WHY**: The majority of our initial QC on digitized files happens on vendor-delivered hard drives or network drives. This results in us needing to change the location of files (from storage media to network, between directories on a single storage, etc) to adhere to our established workflow.

To copy all TIF files from subdirectories in a target directory:

  `find . -name \*.tif -exec /bin/cp {} /TARGETDIR/ \;`

To move (NOT COPY TMP AND DELETE ORIGINAL) preservation master-identified MOV files from subdirectories in a target directory:

  `find . -name \*_pm.mov -exec /bin/mv {} TARGETDIR \;`

###COUNT FILES IN DIRECTORY
**WHY**: The majority of our initial QC on digitized files happens on vendor-delivered hard drives or network drives. This results in us needing to change the location of files (from storage media to network, between directories on a single storage, etc) to adhere to our established workflow. To quickly (not comprehensively) verify that the quantity of files has been copied successfully, it's helpful to have a count of a directory before and after the process is complete.

To find the total of each sub directories and the overall total (Windows) of TIF files:

  In the TARGETDIR, `DIR *.tif /s`

To find the total number of TIF files in a TARGETDIR (the result of this will be +1 the actual number of files):

  In the TARGETDIR, `ls -l dir/*/*.tif | wc -l`

###OUTPUT DIRECTORY TREE
**WHY**: There are instances where creating and validating a disk image are out of scope, and instead we need to copy material, e.g. from a source hard drive or networked drive, to a back up destination. For complex folder hierarchies, it is helpful to have two plain-text directory tree outputs to compare to help identify inconsistencies on a large scale. With these files, we use many comparison strategies, including [Diff Checker](https://www.diffchecker.com). 

To create a directory tree, we use the `ls` command in this way:

  `cd /TARGETDIR/`
  
  `ls -RF > ~/DESTINATION/folderlist.txt`

###CONCATENATE MULTIPLE CSV FILES
**WHY**: In the QC workflow, we break down our digitized material into managable chunks for manual and batch procedures. To create a unified metadata spreadsheet for ingest into our DAMS, we need to be able to combine all disparate spreadsheets in a target grandparent directory into a single CSV with a specific format and prefix in the filename as part of our ingest procedures.

To combine all CSVs in subdirectories into one CSV with desried filenaming convention:

  `cd /TARGETDIR/`
  
  `cat /TARGETDIR/*/*.csv > Central_OPASmatchedFiles_[HDD-ID_volume].csv`

###AUDIT ADMINISTRATIVE METADATA IN VIDEO
**WHY**: When using a vendor to digitize, it is necessary to QC the metadata embedded into a file in addition to the checks to ensure the file opens, passes playback, contains expected audio and video streams, etc. For our preservation masters, CH required certain fields contain specific copyright and producer metadata. To determine completeness/accuracy, we review sample reports from [Exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool/).

  `exiftool -csv -T -Producer -Copyright hddDir > VERIFY_embedmetadata_[HHD-ID_volume].csv`
  
- Open `VERIFY_embedmetadata_[HDD-ID_volume].csv` in Excel
- Verify that # of files match
- Put filter on each column
- Review any inconsitencies
- If modifications are necessary, see EMBED ADMINISTRATIVE METADATA IN VIDEO 

###EMBED ADMINISTRATIVE METADATA IN VIDEO
**WHY**: When using a vendor to digitize, it is necessary to QC the metadata embedded into a file in addition to the checks to ensure the file opens, passes playback, contains expected audio and video streams, etc. For our preservation masters, CH required certain fields contain specific copyright and producer metadata. When issues with this metadata are found (inaccurate, incomplete, or missing) we use [Exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool/) to embed these fields with the desired information. 

We use the `overwrite_original_in_place` because it allows the original files' attributes to be preserved (including original file creation date, type, etc). From the Exiftool documentation, this process happens "by opening the original file in update mode and replacing its data with a copy of a temporary file before deleting the temporary. The extra step results in slower performance, so the -overwrite_original option should be used instead unless necessary." NB: It takes a few hours per 100GB video.

We chose to use this time-intensive process because testing with [FFmpeg](https://ffmpeg.org/) and hex editors was inconsistent and generally introduced significant encoding and stabilization issues. Many thanks to [Xin Fang](https://github.com/xinfang1993) for support in this testing.

To embed producer and copyright statement in ALL preservation master-identified MOV files in a directory:

  `exiftool -Producer="Carnegie Hall Archives" -Copyright="© 201# Carnegie Hall Archives" -overwrite_original_in_place TARGETDIR/*_pm.mov`
  
To embed producer and copyright statement in one MOV file (with sample metadata):

  `exiftool -Producer="Carnegie Hall Archives" -Copyright="© 2016 Carnegie Hall Archives" -overwrite_original_in_place file.mov`

###CREATE GIF FROM STILL IMAGES
**WHY**: Who doesn't love a good GIF? 

Using ImageMagick (already installed, or use `brew install imagemagick` if you have Homebrew):

  `cd [directory of images to be made into GIF]`
  
  `convert *.jpg out.gif`
  
  If you want to add a nice delay/reduce FPS, try:
  
  `convert -delay 20 *.jpg out2.gif`

###REDACT VISUAL CONTENT FROM STILL IMAGES
**WHY**: In an effort to balance access with privacy, there are situations where some pieces of information much be visually redacted from still image archival materials. We use Adobe Acrobat's redaction tool to change pixels in the image to black so that content like personal phone numbers or email addresses are visually obscured in access copies. 

*FYI - THIS PROCESS DOES NOT OBSCURE POTENTIALLY SENSITIVE METADATA LIKE GEOLOCATIONS OR DATES* - it only enables blocked viewing of  'redacted' visual content.

1. Open file(s) you want to redact information from in Adobe Acrobat (CH is using v.10.1.16).
2. Click on *TOOLS* and under _Black Out & Remove Content_, click *Mark for Redaction*.
3. Drag a box around the areas of content you want to black out in the image. For handwritten notes, try to reduce the amount of other information that is obscured by the redaction box so you are not execessively redacting non-sensitive information. This may mean you should use multiple, smaller boxes to avoid blacking out large swathes of information that should be accessible.
4. After the identified content is surrounded by the red boxes, under _Black Out & Remove Content_, click *Apply Redaction*. This will turn your red outlined boxes into black filled DRAFT redactions. It's not final yet! One more step...
5. Click _File_ > _Save_ or _Save As_ and name as appropriate in the preferred destination. Now the pixels representing the sensitive information have been overwritten with black. Check it out!

##LICENSE INFORMATION
_The MIT License (MIT)_

_Copyright (c) 2016 Carnegie Hall_

All contents are released under the terms described in the [MIT License](https://github.com/CarnegieHall/quality-control/blob/master/LICENSE) included in this repository.
