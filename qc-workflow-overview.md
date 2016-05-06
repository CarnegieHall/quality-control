# DAP QC Workflow
|Step #|Phase|File Location|Activity|Tools|Notes|
| ---- |:---:|:-----------:|:------:|:---:|:---:|
|QC-001|Receive HDD from vendor|Vendor harddrive|	Make sure both the HDD and the box are labeled with content, vendor, and date information.| | |		
|QC-002|Receive HDD from vendor|Vendor harddrive|	Verify content on the drive matches what the vendor was supposed to send.| | |		
|QC-003|Receive HDD from vendor|Vendor harddrive|	Confirm with vendor that the HDD was safely received. If there are missing files on the HDD, notify the vendor in writing immediately.| | |			
|QC-004|Integrity checking|Vendor harddrive|Generate CHECKSUM A on all files on HDD|[md5Scrape.py](https://github.com/CarnegieHall/quality-control/blob/master/md5Scrape.py)| |			
|QC-005|Basic QC|Vendor harddrive|Perform aural and visual QC review on selected files (25% - beginning, middle, and end of file)||They mark if files don't align with FNC (but don't change it). Sometimes the date is off, or cha instead of CH. KG must review FOR REVIEW files.|
|QC-006|Metadata QC|Vendor harddrive|Validate the technical metadata.|MDQC| |		
|QC-007|Transfer|Vendor harddrive|Transfer files from HHD to Server| | |
|QC-008|Integrity checking|Server|Generate CHECKSUM B on all transferred files on Server|[md5Scrape.py](https://github.com/CarnegieHall/quality-control/blob/master/md5Scrape.py)||	
|QC-009|Integrity checking|Server|Run checksum validation script (checksum_validation.py) that compares CHECKSUM A (HDD) with CHECKSUM B (Server)|[checksumValidation.py](https://github.com/CarnegieHall/quality-control/blob/master/checksumValidation.py)|	|	
|QC-010|Filename audit/metadata matching|Vendor harddrive|Run Python matching script which identifies unmatched files and associates filenames with OPAS metadata. This script also identifies unmatched OPAS ID's to be cross checked with programs to ensure no programs are missing from the digitized list. Filenames are modified.|[reconcileList.py](https://github.com/CarnegieHall/quality-control/blob/master/reconcileList.py)| |	
|QC-011|Embed metadata|Server|Embed selected metadata field values into audio, video, still images|[embedCopyrightMetadata.sh](https://github.com/CarnegieHall/quality-control/blob/master/embedCopyrightMetadata.sh)| |			
|QC-012|Cortex ingest prep|Server|Create Central CSV for ingest mapping template| | |		
|QC-013|Cortex ingest prep|Server|Copy to Asset_Staging and collapse HDD-dictated hierarchy| | |			
