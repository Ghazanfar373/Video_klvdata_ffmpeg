import subprocess
import klvdata
import pprint
import cv2 as cv # type: ignore
#import imageio

video_path = "/home/serb/DayFlight.mpg"

#Load the video
#reader = imageio.get_reader(video_path, 'ffmpeg')
reader = cv.VideoCapture(video_path)

while reader.isOpened():
	ret, frame = reader.read()
	if not ret:
		break
	# convert frame to a suitabel format for opencv
	#frame_bgr = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
	
    
    #extract klv data
	#klv_stream = klvdata.StreamParser(frame)
	#for packet in klv_stream:
	#	pprint.pprint(packet)

    #cv.imshow('img', frame)
	cv.waitkey(1)
	cv.imshow(frame)
if cv.waitkey(1) & 0xFF == ord('q'):
    exit

reader.release()
cv.destroyAllWindows()
#Extract KLV Data from frame
#for packet in klvdata.StreamParser(video_path):
    # packet.structure()
	#metadata=packet.MetadataList()
	#pprint.pprint(metadata)
    #subprocess.run(['ffplay', video_path])