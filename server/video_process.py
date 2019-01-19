import cv2
import youtube_dl
import numpy as np
import os
import time

FLASH_MINIMUM = 3

tmp_dir = 'temp/'

ex = {'format': 'worstvideo[vcodec^=avc1][fps=30]/worst[vcodec^=avc1][fps=30]/worstvideo[vcodec=vp9][fps=30]/worst[vcodec=vp9][fps=30]', 'outtmpl': 'temp/temp.%(ext)s', 'recode_video': 'webm'}
ytdl = youtube_dl.YoutubeDL(ex)

if not os.path.isdir(tmp_dir):
    os.mkdir(tmp_dir)


def clear_tmp():
    dirs = os.listdir(tmp_dir)
    for d in dirs:
        os.remove(tmp_dir + d)


def dl_tmp(url):
    clear_tmp()
    try:
        ytdl.download([url])
        return 0
    except youtube_dl.utils.DownloadError:
        return 1


def get_tmp():
    files = os.listdir(tmp_dir)
    if len(files) == 1:
        return tmp_dir + files[0]


def process_video(path):
    flash_distance = 0
    cap = cv2.VideoCapture(path)
    frames = []
    flashes = []
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            if flashes:
                flash_distance += 1

            if not ret or cv2.waitKey(1) & 0xFF == ord('q'):
                break
            frames.append(frame.astype(np.int16))
            if len(frames) > 3:
                frames.pop(0)

                # get the net color change in pixel values
                difference = np.abs(np.subtract(frames[2], frames[0]))
                avg_color_change = np.mean(np.sum(difference, axis=2))
                # average = np.mean(difference)

                if avg_color_change > 200:
                    flashes.append(flash_distance)
                    flash_distance = 0
                    frames.pop(0)

        else:
            cap.release()
    return is_dangerous(flashes)


def process_video_url(link):
    if dl_tmp(link) == 1:
        print("Video could not be downloaded properly")
        return

    return process_video(get_tmp())


def is_dangerous(flash_data):
    num_flashes = len(flash_data)
    if num_flashes == 0:
        return False
    avg_flash_distance = np.mean(flash_data)

    # print(num_flashes)
    # print(avg_flash_distance)

    if (num_flashes >= FLASH_MINIMUM) and (num_flashes/avg_flash_distance) > 1:
        return True
    return False


# https://www.youtube.com/watch?v=atkD-beZ9oI # baseline test
# https://www.youtube.com/watch?v=Yw_YDvLWKnY # surreal video
# https://www.youtube.com/watch?v=OCpzajWSp6I # mlg video
# https://www.youtube.com/watch?v=FVY5uZ18-x8 #pokemon video


def main():
    start = time.time()
    results = process_video_url('https://www.youtube.com/watch?v=Yw_YDvLWKnY')
    elapsed = time.time() - start
    print(results)
    print(elapsed)


if __name__ == '__main__':
    main()
