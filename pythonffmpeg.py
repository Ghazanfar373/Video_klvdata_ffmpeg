import ffmpeg
import numpy as np
import cv2
import subprocess


def read_video(video_path):
    cmd = ['ffmpeg', '-i', video_path, '-f', 'rawvideo', '-pix_fmt', 'bgr24', 'pipe:1']
    # process = (
    #     ffmpeg
    #     .i(video_path)
    #     .output('pipe', format='rawvideo')
    #     .run_async(pipe_stdout=True)
    # )
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    width, height = 1280, 720
    while True:
        in_bytes = process.stdout.read(width * height * 3)
        if not in_bytes:
            break

        #Convert the byte data to numpy array
        frame = np.frombuffer(in_bytes, np.uint8).reshape([height, width, 3])

        cv2.imshow('Video', frame)

        #break loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    process.stdout.close()
    cv2.destroyAllWindows()


if __name__== "__main__":
    video_path = "videoSamples/dayflight.mpg"
    read_video(video_path)