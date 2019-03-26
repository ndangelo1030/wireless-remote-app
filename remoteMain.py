#remote main
import os
import sys

def volumeControls():
    #open volume
    print("Opening volume control")
    return

def playbackOptions():
    #open playback control
    print("Opening playback control")
    return 

#main
count = 0

while count ==0:
    choice = int(input("1. Volume control \n 2. playback options \n 3. exit \n"))

    if (choice == 1):
        volumeControls()

    if (choice == 2):
        playbackOptions()

    if (choice == 3):
        break

