from cv2 import VideoCapture
from cv2 import imshow
import pprint
import klvdata
video_path = "/home/serb/DayFlight.mpg"

capture = VideoCapture(video_path)
if not capture.isOpened():
    print("Error establishing connection")
while capture.isOpened():
    ret, frame = capture.read()

    klv_stream = klvdata.StreamParser(frame.tobytes())
    for packet in klv_stream:
        # packet.structure()
        metadata=packet
        if(metadata is not None):
            pprint.pprint(metadata)
        #break
    if ret:
        imshow('Displaying image frames from a webcam', frame)
    #if imshow.waitKey(25) & 0xFF == ord('q'):
    #   break