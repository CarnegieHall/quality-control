
#tech-notes

##USE CASES

###COPY FILES FROM SUBDIRECTORIES
To copy all TIF files from subdirectories in a target directory:

  `find . -name \*.tif -exec /bin/cp {} /TARGETDIR/ \;`

To move (NOT COPY TMP AND DELETE ORIGINAL) preservation master-identified MOV files from subdirectories in a target directory:

  `$ find . -name \*_pm.mov -exec /bin/mv {} TARGETDIR \;`


##LICENSE INFORMATION
_The MIT License (MIT)_

_Copyright (c) 2016 Carnegie Hall_

All contents are released under the terms described in the [MIT License](https://github.com/CarnegieHall/quality-control/blob/master/LICENSE) included in this repository.
