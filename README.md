# Video and KLV Data Stream Processor

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Overview

This script processes a video file containing both video frames and KLV (Key-Length-Value) metadata
using FFmpeg. It simultaneously extracts and displays video frames while parsing KLV data.

## Dependencies

- ffmpeg-python
- OpenCV (cv2)
- klvdata
- numpy

## Installation

pip install ffmpeg-python opencv-python klvdata numpy

## Usage

Ensure the video file path is correctly set in `video_path` variable.
Run the script to display video frames and print KLV metadata.

- python3 multistreamsffmpeg.py
- python3 pipeQueue.py
- python3 klvdata_test.py
- python3 streamffmpeg.py
- python3 switch_views.py

## Features

- Concurrent processing of video and KLV streams
- Real-time video display
- KLV metadata extraction and parsing
- Configurable video dimensions (currently set to 1280x720)

## Controls

- Press 'q' to exit the video display

## Technical Details

- Video Format: Raw video in BGR24 pixel format
- KLV Stream: Copied as raw data
- Frame Processing: Converts byte data to numpy arrays for display
- Video Display: Uses OpenCV for frame rendering

## Example

video_path = "videoSamples/dayflight.mpg"

# Script will process this video file and display frames while extracting KLV data
```

## Note

Ensure the video file contains KLV metadata stream for proper functionality.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
