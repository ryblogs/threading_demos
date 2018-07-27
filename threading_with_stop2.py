# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:24:15 2018

@author: ryblog
"""

import threading
import time

def do_work(id, stop):
    while True:
        print('I am thread %d doing something' % id)
        time.sleep(0.1)
        if stop():
            print('  Exiting loop.\n')
            break
    print('Thread %d, signing off\n' % id)


def main():
    stop_threads = False
    workers = []
    for id in range(0,3):
        tmp = threading.Thread(target=do_work, args=(id, lambda: stop_threads))
        workers.append(tmp)
        tmp.start()
    time.sleep(3)
    print('main: done sleeping; time to stop the threads.')
    stop_threads = True
    for worker in workers:
        worker.join()
    print('Finish.')

if __name__ == '__main__':
    main()