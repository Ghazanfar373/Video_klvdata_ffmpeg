import ffmpeg
import numpy as np
import cv2
import subprocess
import klvdata
import pprint

def read_video(video_path):
#Run the ffmpeg command
    cmd = ['ffmpeg', '-i', video_path, '-map', '0:v', '-f', 'rawvideo', '-pix_fmt', 'bgr24', 'pipe:1', '-map', '0:d', '-f', 'data', 'pipe:2']
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #out,err = process.communicate()
    width, height = 1280, 720
    while True:
        in_bytes = process.stdout.read(width * height * 3)
        if not in_bytes:
            break

        #Convert the byte data to numpy array
        frame = np.frombuffer(in_bytes, np.uint8).reshape([height, width, 3])

        #Read Klv Data
        klv_bytes = process.stderr.read(188)
        klv_stream = klvdata.StreamParser(klv_bytes)
        #for packet in klv_stream:
            #pprint.pprint(packet)
            #break

        cv2.imshow('Video', frame)

        #break loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    process.stdout.close()
    cv2.destroyAllWindows()


if __name__== "__main__":
    video_path = "videoSamples/dayflight.mpg"
    read_video(video_path)


 