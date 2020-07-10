#!/usr/bin/python3
''' itsOrD || basic threading in python '''

## Thread that simulates a NASA countdown & waits 1 sec at the end of each loop

import threading
import time

def groundcontrol():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

print ("Dragon, you're ready for launch sequence. Count down starting...")

## create a thread object (target is the function to call)
mythread = threading.Thread(target=groundcontrol)

## begin the thread
mythread.start()

