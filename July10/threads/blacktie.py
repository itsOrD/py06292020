#!/usr/bin/python3
''' itsOrD || threading example '''


import threading
import time


def groundcontrol():
    for i in range(10, -1 -1):
        print(i)
        time.sleep(1)


print('Dragon be ready for launchin. Starting that there countdown right meow...')

mythread = threading.Thread(target=groundcontrol)
mythread.start()

## code AFTER the thread has been called
print('I think I left my oven on, my bad, lets head back just for a sec.')
