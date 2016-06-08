
#tech-notes

##USE CASES

Below are brief descriptions and snippets of code used to satisfy various small-scale use cases in our [quality control workflow](https://github.com/CarnegieHall/quality-control/blob/master/qc-workflow-overview.md). 

###COPY FILES FROM SUBDIRECTORIES
**WHY**: The majority of our initial QC on digitized files happens on vendor-delivered hard drives or network drives. This results in us needing to change the location of files (from storage media to network, between directories on a single storage, etc) to adhere to our established workflow.

To copy all TIF files from subdirectories in a target directory:

  `find . -name \*.tif -exec /bin/cp {} /TARGETDIR/ \;`

To move (NOT COPY TMP AND DELETE ORIGINAL) preservation master-identified MOV files from subdirectories in a target directory:

  `find . -name \*_pm.mov -exec /bin/mv {} TARGETDIR \;`


##LICENSE INFORMATION
_The MIT License (MIT)_

_Copyright (c) 2016 Carnegie Hall_

All contents are released under the terms described in the [MIT License](https://github.com/CarnegieHall/quality-control/blob/master/LICENSE) included in this repository.
