import datetime

import Process

if __name__ == "__main__":

    now = datetime.datetime.now()
    Process.process(1,1000)
    finish = datetime.datetime.now() - now
    print(f'Time to finish Cython {finish}')


"""
Result
Time to finish Cython 0:00:00.000050
"""