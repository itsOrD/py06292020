#!/usr/bin/python3
''' itsOrD || thread with join '''


import threading
import time


def groundcontrol():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

print("Dragon's gonna launch...")

mythread = threading.Thread(target=groundcontrol)
mythread.start()

print('Ah! I forgot my spacesuit!')

# wait until the threads finish before moving on
mythread.join()

# aks user to press a key to exit
input('Press enter to exit.')
exit()
