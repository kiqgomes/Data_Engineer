import threading
import time 

def countName(name,num):
    for n in range(1,num+1):
        print(f'{name} and {n}')
        time.sleep(2)

def thread():
    th = threading.Thread(target=countName,args=('Kaique',10))
    
    print('Starting process')
    th.start()
    
    print('Working ....')

    th.join()

    print('Done')

if __name__ == '__main__':
    thread()