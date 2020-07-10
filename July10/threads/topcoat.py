#!/usr/bin/python3
''' itsOrD || multithread '''


import threading
import time


def groundcontrol(x):
    for i in range(x, -1, -1):
        print(i)
        time.sleep(1)

def dragon():
    print('...forgot my socks...')
    time.sleep(1)
    print('--can we stop?--')
    time.sleep(2)
    print('++No!? Fine...++')
    time.sleep(1)
    print('==Buzz, buzz fizz==')

print('Dragon launching......')

countycount = 7

mythread = threading.Thread(target=groundcontrol, args=(countycount, ))
astrothread = threading.Thread(target=dragon)

mythread.start()
astrothread.start()

mythread.join()
astrothread.join()

input('Press that there Enter to exit')
exit()
