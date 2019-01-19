import cv2
import youtube_dl
import numpy as np
import os
import time
tmp_dir = 'temp/'
ex = {'format': 'worstvideo', 'outtmpl': 'temp/temp.%(ext)s'}
ytdl = youtube_dl.YoutubeDL(ex)


def clear_tmp():
    dirs = os.listdir(tmp_dir)
    for d in dirs:
        os.remove(tmp_dir + d)


def dl_tmp(url):
    clear_tmp()
    ytdl.download([url])


def get_tmp():
    files = os.listdir(tmp_dir)
    if len(files) == 1:
        return tmp_dir + files[0]


def process_video(path):
    counter = 0
    cap = cv2.VideoCapture(path)
    frames = []
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Display the resulting frame
            # cv2.imshow('frame', frame)
            if not ret or cv2.waitKey(1) & 0xFF == ord('q'):
                break
            frames.append(frame)
            if len(frames) > 3:
                frames.pop(0)
                difference = np.mean(np.abs(frames[2] - frames[0]))
                if difference < 200:
                    counter += 1
                    cv2.imshow('frame', frames[0])
                    cv2.imshow('frame', frames[2])

        else:
            print(counter)
            cap.release()

#dl_tmp('https://www.youtube.com/watch?v=atkD-beZ9oI')
#dl_tmp('https://www.youtube.com/watch?v=4N0qwuG3MaY')
start = time.time()
process_video(get_tmp())
elapsed = time.time() - start
print(elapsed)
