"""
For this program to run smoothly with vlc a few things needs to be changed on VLC's settings :
1 - remove vlc video title from startup
2 - Remove VLC media controllers from fullscreen video
3 - Close VLC when playlist ends
4 - Set the RUN_VLC global variable to be "vlc " if the cmd has the command vlc otherwise the path to vlc application file followed by a space.
"""
import os
import random
import multiprocessing
import time

import pygetwindow as gw

KILL_MEDIA = "0"
COMMERCIAL = "1"
TRAILER = "2"
INTRO = "3"
EXIT = "9"

QUIT_VLC = "pkill \"VLC\""
RUN_VLC = "/Applications/VLC.app/Contents/MacOS/VLC "
HIDECMD = "  > /dev/null 2>&1"


def setFocusToConsole():
    """
    Only works for windows.
    Run must be in window mode.
    :return:
    """
    if not os.name == 'nt':
        return
    time.sleep(1)
    win = gw.getWindowsWithTitle('run')[0]
    win.activate()


def runVideoCMD(vidPath):
    cmd = RUN_VLC + vidPath + HIDECMD
    os.system(cmd)


def runVideoThread(vidPath):
    t1 = multiprocessing.Process(target=runVideoCMD, args=(vidPath,))
    t1.start()
    setFocusToConsole()


def playVideo(path):
    runVideoThread(path)


def getInput():
    # printNextInfo()
    return input("Waiting for input \n")


def printNextInfo(bextCommercial, nextTrailer):
    print("Next Commercial is: " + bextCommercial + "\nNext Trailer Is : " + nextTrailer + "\n")


def removeRedundencies(dir):
    if '.DS_Store' in dir:
        dir.remove('.DS_Store')


def getShuffledPaths(path):
    lst = os.listdir(path)
    removeRedundencies(lst)
    random.shuffle(lst)
    return lst


def mainLoop():
    path_to_commercials = "/Users/tomerlankri/Downloads/commercials"
    path_to_trailers = "/Users/tomerlankri/Downloads/trailers"
    path_to_intros = "/Users/tomerlankri/Downloads/sounds"

    lst_commercials = getShuffledPaths(path_to_commercials)
    lst_trailers = getShuffledPaths(path_to_trailers)
    lst_intro = getShuffledPaths(path_to_intros)

    len_commercials = len(lst_commercials)
    len_trailers = len(lst_trailers)
    len_intros = len(lst_intro)

    commercial_idx = 0
    trailer_idx = 0
    intro_idx = 0

    inputValue = getInput()

    while inputValue and inputValue != EXIT:
        if inputValue == COMMERCIAL:
            path = path_to_commercials + '/' + lst_commercials[commercial_idx]
            playVideo(path)
            commercial_idx = (commercial_idx + 1) % len_commercials

        elif inputValue == TRAILER:
            path = path_to_trailers + '/' + lst_trailers[trailer_idx]
            playVideo(path)
            trailer_idx = (trailer_idx + 1) % len_trailers

        elif inputValue == INTRO:
            path = path_to_intros + '/' + lst_intro[intro_idx]
            playVideo(path)
            intro_idx = (intro_idx + 1) % len_intros

        elif inputValue == KILL_MEDIA:
            killMedia()

        printNextInfo(lst_commercials[commercial_idx], lst_trailers[trailer_idx])
        inputValue = getInput()


def killMedia():
    print("kill Media was requested")
    os.system(QUIT_VLC)


if __name__ == '__main__':
    setFocusToConsole()
    mainLoop()
