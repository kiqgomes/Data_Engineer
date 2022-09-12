from imp import acquire_lock
import threading
import time 

def countName(name,num):
    for n in range(1,num+1):
        print(f'{name} and {n}')
        time.sleep(1)

def thread():
    threads = [
        threading.Thread(target=countName,args=('Kaique',10))
        ,threading.Thread(target=countName,args=('Claudio',8))
        ,threading.Thread(target=countName,args=('Sidney',21))
        ,threading.Thread(target=countName,args=('Pedro',19))
    ]

    print('Starting process')
    [th.start() for th in threads]
    
    print('Working ....')

    [th.join() for th in threads]

    print('Done')

if __name__ == '__main__':
    thread()