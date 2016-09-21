#!/bin/bash
# =============================================
# Checksum Script  
# written by AVPreserve
# 2010-08-11              http://avpreserve.com
# last updated 2016-09-21                    
# =============================================
# requires md5,sha1sum,find,echo,file,basename,stat,date,eval
# setting variables, used in filenaming
# To run, $ ./qa_cksum.sh [content dir] [output destination dir] 0 
# run script with two arguments:
# argument 1 is the directory of content to analyze
# argument 2 is the directory to sending reporting to
# argument 3 is the number of directories down from argument 1 to split output reports into
#variables
# Modified 2015-03-03 by Kathryn Gronsbell, AVPreserve (comment out line 84; not required for CH checksum
# generation and validation process. Requires Excel sheet with formulas to validate from output spreadsheet.)
if [ -z "$3" ]; then
depth=0
else
depth="$3"
fi
find "$1" -maxdepth "$depth" -mindepth "$depth" -type d > "/tmp/subdirs.txt"
cat "/tmp/subdirs.txt" | while read subdir; do
	surdirname=`basename "$subdir"`
	cksum_filename_root="qa"
	scriptdir=`dirname "$0"`
	now=`date "+%Y-%m-%dT%H-%M-%S"`
	today=`date "+%Y-%m-%d"`
	sincefile="${2}/${surdirname}_lastrun"
	outputcsv="${2}/${cksum_filename_root}_${surdirname}_${now}/${cksum_filename_root}_${surdirname}_cksums.csv"
	fillist="${2}/${cksum_filename_root}_${surdirname}_${now}/filelist.txt"
	mkdir -p "${2}/${cksum_filename_root}_${surdirname}_${now}"
	# test for input arguments
	if [ "$#" != 3 ]; then
	    echo The script requires two arguments:
	    echo 1: The directory in which to scan for content to checksum
	    echo 2: A writeable output directory in which to store checksum data in CSV files
	    echo exiting
	    exit 1
	fi
	if [ ! -d "$1" ]; then
	    echo not a directory: $1
	    echo exiting
	    exit 2
	fi
	if [ ! -d "$2" ]; then
	    echo not a directory: $2
	    echo exiting
	    exit 3
	fi
	
	# setting up find options
	find_opts+="-type f ! -name '.*'"
	if [ -e "$sincefile" ]; then
	    find_opts="-type f ! -name '.*' -neweraa '$sincefile' -o -type f ! -name '.*' -newerca '$sincefile' "
	fi
	
	# set up output file of checksum data
	if [ ! -e "$outputcsv" ]; then
	echo "md5,md5_datetime,filename,mime_type,last_modif,path" > "$outputcsv"
	fi
	
	# set lastrun fileh
	eval "find \"${subdir}\" ${find_opts}" > "${fillist}"
	touch "${2}/lastrun"
	cat "${fillist}" | while read file; do
	    #checksum process
	        echo "$file"
        # process md5 and sha1 checksums
        md5=`md5 -q "${file}"`
        md5when=`date "+%Y-%m-%dT%H:%M:%S"`
        echo " md5= ${md5} "
        # sha1=`shasum -a 1 "${file}" | cut -d " " -f 1`
        # sha1when=`date "+%Y-%m-%dT%H:%M:%S"`
        # echo " sha1= ${sha1} "
        # get filename of the file
        filename=`basename "${file}"`
        # get modification timestamp of the file
        lastmod=`stat -x -t "%Y-%m-%dT%H:%M:%S" "${file}" | grep ^Modify | cut -c 9-`
        # get mime type of the file
        mime=`file -Ib "${file}"`
        # report out md5,md5_datetime,sha1,sha1_datetime,filename,mime_type,last_modif,path to output csv file
        echo "${md5},${md5when},${filename},${mime},${lastmod},${file}" >> "$outputcsv"
    # technical metadata process
#"$scriptdir/qa_list_process.sh" "${file}" "${2}/${cksum_filename_root}_${surdirname}_${now}/${cksum_filename_root}_${surdirname}_techmd"
	done
done