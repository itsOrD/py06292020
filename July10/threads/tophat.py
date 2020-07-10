#!/usr/bin/python3
''' itsOrD || threading with pids

Notes:
    - os.getpid() fxn will return ID of current process
    - threading.main_thread() returns the main thread object
      typicaly the main thread is the thread from which Python was started
    - threading.current_thread() returns the current thread object
'''


import threading
import os


def task1():
    print(f'''Task 1 assigned to thread: {threading.current_thread().name}''')
    print(f'''ID of process running task 1: {os.getpid()}''')

def task2():
    print(f'''Task 2 assigned to thread: {threading.current_thread().name}''')
    print(f'''ID of process runing main program: {os.getpid()}''')

def main():
    # print ID of current process
    print(f'''ID of process running main program: {os.getpid()}''')

    # print name of main thread
    print(f'''Main thread name: {threading.main_thread().name}''')

    # create threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    
    # start threads
    t1.start()
    t2.start()

    # wait untill all threads finish
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
