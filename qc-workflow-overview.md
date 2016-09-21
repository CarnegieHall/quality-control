# Digitized Materials Quality Control Workflow

Below is a working draft of the phases and individual steps we take upon receiving digitized material on hard drives from our digitization vendors. For ease and control, batches of information are based on the hard drive they arrived on. We track the progress of the hard drive as it moves through the steps in a shared tracking document, gathering additional information (or exceptions) as necessary. 

The ultimate goal following QC is to move materials into an Asset Staging area, where they will be uploaded, along with any additional metadata records, into our Digital Asset Management System (DAMS) for access and transcoding for distribution. 

|Step #|Phase|File Location|Activity|Tool|
| ---- |:---:|:-----------:|------|:---:|
|QC-001|Receive harddrive from vendor|Vendor harddrive|	Make sure both the harddrive and the box are labeled with content, vendor, and date information. Confirm that what was expected from the vendor was received.|		
|QC-002|Receive harddrive from vendor|Vendor harddrive|	Verify content on the drive matches what the vendor was supposed to send. Refer to the Statement of Work and existing project management documents.|		
|QC-003|Receive harddrive from vendor|Vendor harddrive|	Confirm with vendor that the harrdrive was safely received. If there are missing files on the harddrive, notify the vendor in writing immediately.| ||			
|QC-004|Integrity checking|Vendor harddrive|Generate CHECKSUM A on all files on harrdrive, stored in a CSV file.|[md5Scrape.py](https://github.com/CarnegieHall/quality-control/blob/master/md5Scrape.py) OR [qa_cksum.sh](qa_cksum.sh)|			
|QC-005|Basic QC|Vendor harddrive|Perform aural and visual QC review on selected files (25% of total assets). Identify and flag issues for review.|
|QC-006|Metadata QC|Vendor harddrive|Audit the technical metadata against requested  specifications.|[MDQC](https://github.com/avpreserve/mdqc)||		
|QC-007|Transfer|Vendor harddrive|Transfer files from harddrive to Server| | |
|QC-008|Integrity checking|Server|Generate CHECKSUM B on all transferred files on Server|[md5Scrape.py](https://github.com/CarnegieHall/quality-control/blob/master/md5Scrape.py) OR [qa_cksum.sh](qa_cksum.sh)||	
|QC-009|Integrity checking|Server|Run the script that compares CHECKSUM A (from the harddrive) with CHECKSUM B (on the server) (Server)|[checksumValidation.py](https://github.com/CarnegieHall/quality-control/blob/master/checksumValidation.py)|	|	
|QC-010|Filename audit/metadata matching|Server|Run the script which associates filenames with performance metadata. This script also identifies unmatched event IDs to be cross-checked to ensure no content are missing from the digitized material. Filenames are modified. Does not apply to those files that are not related to events.|[metadata-matching](https://github.com/CarnegieHall/metadata-matching.git)| |	
|QC-011|Embed metadata|Server|Embed selected metadata field values into audio, video, still images|[embedCopyrightMetadata.sh](https://github.com/CarnegieHall/quality-control/blob/master/embedCopyrightMetadata.sh)||			
|QC-012|DAMS ingest prep|Server|Create metadata CSV for DAMS ingest template| | |		
|QC-013|DAMS ingest prep|Server|Copy to the destination folder and collapse harddrive-dictated hierarchy| | |			
