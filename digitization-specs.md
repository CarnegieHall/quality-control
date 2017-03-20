# digitization-specs

## OVERVIEW

In July 2012, Carnegie Hall’s Archives started its Digital Archives Project (DAP), a multi-year initiative that will preserve and digitize most of the Hall’s historic collections. Many of Carnegie Hall’s archival materials—including photographs, program books, flyers, posters, correspondence, and recordings—are currently available only on paper or in media formats that are obsolete or degraded.

Carnegie Hall Archives outsources the majority of its reformatting/digitization work to vendors. Details about how the Archives does quality control on the received files is available in our [quality control workflow document](https://github.com/CarnegieHall/quality-control/blob/master/qc-workflow-overview.md). 

This document describes preservation master (and mezzanine, where applicable) deliverables CH requires from vendors based on physical source format (audio, video, still image) and/or content type (e.g., a concert program page or a flyer). This page does not serve as a list of recommendations, but instead a centralized document to describe the specs that have been dictated to vendors since the inception of the DAP.

## DELIVERABLE SPECS

### Audio

#### Preservation masters: Analog sources (e.g., 1/4” reel to reels)
- Broadcast Wave Format (BWF)
- Audio encoded at 24-bit, 96kHz.
- All BWF header fields should be populated with the appropriate metadata.

#### Preservation masters: Audio from optical sources (CDs)
- Broadcast Wave Format (BWF)
- Audio encoded at 16-bit, 44.1kHz.
- All BWF header fields should be populated with the appropriate metadata.

### Video

#### Preservation video masters:
- QuickTime wrapper (.mov extension)
- Video encoded using the 10-bit YUV 4:2:2 uncompressed codec with the FourCC identifier `v210`.
- Audio encoded as uncompressed PCM audio, 48khz.
- Maintain original aspect ratio, recording standard, interlacing, number of audio channels and ancillary information such as original timecode and closed captioning.
- exception: if source material is low fidelity source (e.g. consumer grade analog videotape), PMs may be digitized to Video mezzanine specs (below).

#### Video mezzanines:
- QuickTime wrapper (.mov extension)
- Video encoded using the FourCC `dvc ` codec.

### Preservation masters from optical sources (DVDs)
- MPEG-2
- 4:2:2, 8-bit

### Motion Picture Film

#### Film preservation masters:
- 2K files (DPX stacks)

#### Film mezzanines:
- QuickTime ProRes 422 HQ, progressive scanning, frame rate: 24 fps, 1920x1080 for 16:9 aspect ratios or 720x486 for 4:3 aspect ratios.

### Still Image - Concert Programs
- 16 bit uncompressed TIFF files, minimum 400 DPI, RGB colorspace

### Still Image - Flyers, Photographs, Ephemera, etc.
- 16 bit uncompressed TIFF files, minimum 600 DPI, RGB colorspace
