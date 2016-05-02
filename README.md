# quality-control

##OVERVIEW
Carnegie Hall Archives maintains a series of small, portable scripts to expedite batch processes for quality control on our Digital Collections.

These scripts have benefitted immensely from a wide community of archiving, preservation, and programming experts who share their code and troubleshooting techniques online. We are excited by the opportunity to participate in this community and have our methods improve through open collaboration and mutual exchange.

##CONTENTS

| Script Name         | Purpose           |
| ------------- |-------------|
|**[checksumValidation.py](https://github.com/CarnegieHall/quality-control/blob/master/checksumValidation.py)**      | Compares two given checksum hashes and outputs log of pass/fail/missing |
|**[md5Scrape.py](https://github.com/CarnegieHall/quality-control/blob/master/md5Scrape.py)** | Scrapes all .md5 sidecar files in a given directory and outputs information into a formatted CSV |
| **[reconcileList.py](https://github.com/CarnegieHall/quality-control/blob/master/reconcileList.py)**     | Compare two lists of files, and output CSV of non-matching values |


##USAGE AND LICENSE
###USAGE GUIDELINES
This code is provided “as is” and for you to use at your own risk. The information included in the contents of this repository is not necessarily complete. Carnegie Hall offers the scripts as-is and makes no representations or warranties of any kind.

We plan to update the scripts regularly. We welcome any [Issues](https://github.com/CarnegieHall/quality-control/issues) and other feedback. Please let us know if you have found the contents of this repository useful!

###LICENSE
_The MIT License (MIT)_

_Copyright (c) 2016 Carnegie Hall_

All contents are released under the terms described in the [MIT License](https://github.com/CarnegieHall/quality-control/blob/master/LICENSE) included in this repository.
