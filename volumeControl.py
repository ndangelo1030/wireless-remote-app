#volume control

import os
import sys

def volumeUp():
    #push volume up to system
    print("Volume up")
    return 

def volumeDown():
    #push volume down to system
    print("Volume down")
    return 

def mute():
    #push mute to system
    print("mute")
    return 


#main
count = 0

while count == 0:
    choice = int(input("1. Volume up \n 2. Volume down \n 3. Mute \n 4. exit volume control \n"))
    print(choice)
    
    if (choice == 1):
        volumeUp()

    if (choice == 2):
        volumeDown()

    if (choice == 3):
        mute()

    if (choice == 4):
        break

