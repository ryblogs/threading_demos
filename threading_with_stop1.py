# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import threading
import time

def func_1(stop):
    i = 0
    while True:
        i += 1
        time.sleep(0.49) # Do some work for 1.5 seconds
        print('func_1')
        if stop():
            break

def func_2(stop):
    i = 0
    while True:
        i += 1
        time.sleep(3) # Do some work for 0.5 seconds
        print('func_2')
        if stop():
            break

stop_threads = False
thread1 = threading.Thread(target=func_1, args=(lambda: stop_threads,))
thread1.start()
thread2 = threading.Thread(target=func_2, args=(lambda: stop_threads,))
thread2.start()
time.sleep(5)
stop_threads = True
thread1.join()
thread2.join()
print('Finish.')



















































