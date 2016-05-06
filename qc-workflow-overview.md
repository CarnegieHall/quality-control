# DAP QC Workflow
|Step #|Phase|File Location|Activity|Tools|Notes|
| ---- |:---:|:-----------:|:------:|:---:|:---:|
|QC-001|Receive HDD from vendor|Vendor harddrive|	Make sure both the HDD and the box are labeled with content, vendor, and date information.| |Confirm that what was expected from the vendor was received.|		
|QC-002|Receive HDD from vendor|Vendor harddrive|	Verify content on the drive matches what the vendor was supposed to send.| |Using the Statement of Work to check if there is any file missing.|		
|QC-003|Receive HDD from vendor|Vendor harddrive|	Confirm with vendor that the HDD was safely received. If there are missing files on the HDD, notify the vendor in writing immediately.| |Talk to vendor if there is any problem.|			
|QC-004|Integrity checking|Vendor harddrive|Generate CHECKSUM A on all files on HDD|[md5Scrape.py](https://github.com/CarnegieHall/quality-control/blob/master/md5Scrape.py)|All the checksum generated should be stored in a csv. file|			
|QC-005|Basic QC|Vendor harddrive|Perform aural and visual QC review on selected files (25% - beginning, middle, and end of file)||Point out all sorts of question such as the file name, date.|
|QC-006|Metadata QC|Vendor harddrive|Validate the technical metadata.|[MDQC](https://github.com/avpreserve/mdqc)||		
|QC-007|Transfer|Vendor harddrive|Transfer files from HHD to Server| | |
|QC-008|Integrity checking|Server|Generate CHECKSUM B on all transferred files on Server|[md5Scrape.py](https://github.com/CarnegieHall/quality-control/blob/master/md5Scrape.py)|Again, the checksum should be stored in another csv. file.|	
|QC-009|Integrity checking|Server|Run the script that compares CHECKSUM A (HDD) with CHECKSUM B (Server)|[checksumValidation.py](https://github.com/CarnegieHall/quality-control/blob/master/checksumValidation.py)|	|	
|QC-010|Filename audit/metadata matching|Vendor harddrive|Run the script which identifies unmatched files and associates filenames with OPAS metadata. This script also identifies unmatched OPAS ID's to be cross checked with programs to ensure no programs are missing from the digitized list. Filenames are modified.|[reconcileList.py](https://github.com/CarnegieHall/quality-control/blob/master/reconcileList.py)| |	
|QC-011|Embed metadata|Server|Embed selected metadata field values into audio, video, still images|[embedCopyrightMetadata.sh](https://github.com/CarnegieHall/quality-control/blob/master/embedCopyrightMetadata.sh)|Does not apply to those files that do not have OPAS IDs.|			
|QC-012|DAMS ingest prep|Server|Create Central CSV for ingest mapping template| | |		
|QC-013|DAMS ingest prep|Server|Copy to the destinate folder and collapse HDD-dictated hierarchy| | |			
