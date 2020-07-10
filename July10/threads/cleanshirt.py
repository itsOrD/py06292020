#!/usr/bin/python3
''' itsOrD || threading with an exit '''


import threading
import time


def groundcontrol():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

print("Dragon's launching...")

mythread = threading.Thread(target=groundcontrol)
mythread.start()

input('Press Enter to exit...')
exit()
