#!/bin/bash
# ----Copyright (c) 2016 Carnegie Hall | The MIT License (MIT)----
# ----For the full license terms, please visit https://github.com/CarnegieHall/quality-control/blob/master/LICENSE----
# argument 1 is the directory to be scanned (the script will find all files in any subdirectory)


CREATOR="Carnegie Hall Archives"
COPYRIGHTNOTICE="© 2015 Carnegie Hall Archives"

echo The values to be embedded in files appears in $1 are: $CREATOR and $COPYRIGHTNOTICE
while true; do
    read -p "Do you want to embed $CREATOR and $COPYRIGHTNOTICE? (y/n)" yn
    case $yn in
        [Yy]* ) exiftool -creator="$CREATOR" -copyrightnotice="$COPYRIGHTNOTICE" -overwrite_original "$1"/*/; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

