from concurrent.futures import thread
import queue
import time
import colorama

from threading import Thread
from queue import Queue

def data_generator(queue: Queue):
    for i in range(1,11):
         print(colorama.Fore.GREEN + f'Data generated {i}.',flush=True)
         time.sleep(2)
         queue.put(i)

def data_user(queue: Queue):
    while queue.qsize() > 0:
        value = queue.get()
        print(colorama.Fore.RED + f'Data processed {value * 2 }.',flush=True)
        time.sleep(1)
        queue.task_done()

if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Initiating system ...',flush=True)
    queue = Queue()

    th_fi = Thread(target=data_generator,args=(queue,))
    th_se = Thread(target=data_user,args=(queue,))

    print(colorama.Fore.BLUE + 'Starting the first thread ...')
    th_fi.start()

    th_fi.join()

    print(colorama.Fore.BLUE + 'Starting the second one ...')
    th_se.start()

    th_se.join()