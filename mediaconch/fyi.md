To **run MediaConch on audiovisual files**, do:

`$ mediaconch -p policyfile -fa path/to/files/*_pm.mov > path/to/reports/MediaConchReport_VENDOR_YEAR#_DRIVE-ID.xml`

To see a quick summary of **how many files passed or failed** the invoked policy in Terminal, do:

`$ cd ~/qualitycontrol/mediaconch`

`$ python3 mediaconch-xmlreport-summary.py path/to/reports/MediaConchReport_VENDOR_YEAR#_DRIVE-ID.xml`


