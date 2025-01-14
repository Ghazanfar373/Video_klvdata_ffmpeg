import subprocess
import numpy as np
import cv2
import klvdata
import threading
import queue
import pprint

def read_video_frames(process, frame_queue, width, height):
    while True:
        in_bytes = process.stdout.read(width * height * 3)
        if not in_bytes:
            break
        frame = np.frombuffer(in_bytes, np.uint8).reshape([height, width, 3])
        frame_queue.put(frame)
    process.stdout.close()

def read_klv_data(process, klv_queue):
    while True:
        klv_bytes = process.stderr.read(250)  # Adjust the packet size as needed
        if not klv_bytes:
            break
        klv_queue.put(klv_bytes)
    process.stderr.close()

def main():
    video_path = "videoSamples/dayflight.mpg" # Replace with the path to your MPEG video file
    width, height = 1280, 720  # Adjust these values according to your video resolution

    command = [
        'ffmpeg', '-i', video_path,
        '-map', '0:v', '-f', 'rawvideo', '-pix_fmt', 'bgr24', 'pipe:1',
        '-map', '0:d', '-f', 'data', 'pipe:2'
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    frame_queue = queue.Queue()
    klv_queue = queue.Queue()

    video_thread = threading.Thread(target=read_video_frames, args=(process, frame_queue, width, height))
    klv_thread = threading.Thread(target=read_klv_data, args=(process, klv_queue))
    
    video_thread.start()
    klv_thread.start()

    with open('klv_data.txt', 'w') as klv_file:
        while video_thread.is_alive() or not frame_queue.empty():
            if not frame_queue.empty():
                frame = frame_queue.get()
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            if not klv_queue.empty():
                klv_bytes = klv_queue.get()
                try:
                    klv_stream = klvdata.StreamParser(klv_bytes)
                    for packet in klv_stream:
                    #klv_file.write(str(packet) + '\n')
                    #pprint.pprint(str(packet) + '\n')
                    
                        pprint.pprint(packet)
                except Exception as e:
                    pprint.pprint("Error parsing klv data {e}")

    cv2.destroyAllWindows()
    video_thread.join()
    klv_thread.join()

if __name__ == "__main__":
    main()
