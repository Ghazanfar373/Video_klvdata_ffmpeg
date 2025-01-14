import ffmpeg
import cv2
import klvdata
import numpy as np
import pprint

# Define the path to your video file
video_path = "videoSamples/dayflight.mpg"

# Open the video file using FFmpeg
stream = ffmpeg.input(video_path)

# Extract video and KLV data streams
video_stream = stream['v']
klv_stream = stream['d']

# Open a file to write KLV data
#with open('klv_data.txt', 'w') as klv_file:
process_video = ffmpeg.output(video_stream, 'pipe:1', format='rawvideo', pix_fmt='bgr24')
process_klv = ffmpeg.output(klv_stream, 'pipe:2', codec='copy', format='data')

# Run processes asynchronously
process_video = process_video.run_async(pipe_stdout=True)
process_klv = process_klv.run_async(pipe_stdout=True)

# Create KLV parser
klv_parser = klvdata.StreamParser(process_klv.stdout)
width, height = 1280, 720
while True:
    # Read video frame
    in_bytes = process_video.stdout.read(width * height * 3)
   #Convert the byte data to numpy array
    if not in_bytes:
            break
    frame = np.frombuffer(in_bytes, np.uint8).reshape([height, width, 3])

    # Extract KLV data from the frame bytes
    klv_data = next(klv_parser, None)
    if klv_data:
        pprint.pprint(str(klv_data) + '\n')

    # Display the frame using OpenCV
    cv2.imshow('Video', frame)

    # Break the loop on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
process_video.stdout.close()
process_klv.stdout.close()
cv2.destroyAllWindows()