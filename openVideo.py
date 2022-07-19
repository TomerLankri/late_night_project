import multiprocessing

import main

WIDTH = 400
HEIGHT = 400
import time
import cv2
import vlc
import os
QUIT_VLC = "pkill \"VLC\""
RUN_VLC = "/Applications/VLC.app/Contents/MacOS/VLC "
HIDECMD ="  > /dev/null 2>&1"

def runVideo(vidPath):
    file_name = vidPath
    window_name = "window"

    interframe_wait_ms = 30

    cap = cv2.VideoCapture(file_name)
    cap.set(3,WIDTH)
    cap.set(4,HEIGHT)

    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while (True):
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video, exiting.")
            break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(interframe_wait_ms) & 0x7F == ord(main.EXIT):
            print("Exit requested.")
            break

    cap.release()
    cv2.destroyAllWindows()

def runVideo2(vidPath):
    cmd = RUN_VLC + vidPath + HIDECMD
    os.system(cmd)

def do():
    print("doing")

def runVideo3(vidPath):
    t1 = multiprocessing.Process(target=runVideo2, args=(vidPath,))
    t1.start()


if __name__ == '__main__':


    runVideo3("/Users/tomerlankri/Downloads/trailers/trailer1.mp4")
    input("what")
    os.system(QUIT_VLC)
    input("aaa")
