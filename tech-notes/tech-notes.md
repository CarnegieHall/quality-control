
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

###CONCATENATE MULTIPLE CSV FILES
**WHY**: In the QC workflow, we break down our digitized material into managable chunks for manual and batch procedures. To create a unified metadata spreadsheet for ingest into our DAMS, we need to be able to combine all disparate spreadsheets in a target grandparent directory into a single CSV with a specific format and prefix in the filename as part of our ingest procedures.

To combine all CSVs in subdirectories into one CSV with desried filenaming convention:

  `cd /TARGETDIR/`
  
  `cat /TARGETDIR/*/*.csv > Central_OPASmatchedFiles_[HDD-ID_volume].csv`

###EMBED ADMINISTRATIVE METADATA INTO VIDEO
**WHY**: When using a vendor to digitize, it is necessary to QC the metadata embedded into a file in addition to the checks to ensure the file opens, passes playback, contains expected audio and video streams, etc. For our preservation masters, CH required certain fields contain specific copyright and producer metadata. When issues with this metadata are found (inaccurate, incomplete, or simply missing) we use [Exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool/) to embed these fields with the desired information. 

We use the `overwrite_original_in_place` because it allows the original files' attributes to be preserved (including original file creation date, type, etc). From the Exiftool documentation, this process happens "by opening the original file in update mode and replacing its data with a copy of a temporary file before deleting the temporary. The extra step results in slower performance, so the -overwrite_original option should be used instead unless necessary." NB: It takes a few hours per 100GB video.

We chose to use this time-intensive process because testing with [FFmpeg](https://ffmpeg.org/) and hex editors was inconsistent and generally introduced significant encoding and stabilization issues. Many thanks to [Xin Fang](https://github.com/xinfang1993) for support in this testing.

To embed producer and copyright statement in ALL preservation master-identified MOV files in a directory:

  `exiftool -Producer="Carnegie Hall Archives" -Copyright="© 201# Carnegie Hall Archives" -overwrite_original_in_place TARGETDIR/*_pm.mov`
  
To embed producer and copyright statement in one MOV file (with sample metadata):

  `exiftool -Producer="Carnegie Hall Archives" -Copyright="© 2016 Carnegie Hall Archives" -overwrite_original_in_place file.mov`


##LICENSE INFORMATION
_The MIT License (MIT)_

_Copyright (c) 2016 Carnegie Hall_

All contents are released under the terms described in the [MIT License](https://github.com/CarnegieHall/quality-control/blob/master/LICENSE) included in this repository.
