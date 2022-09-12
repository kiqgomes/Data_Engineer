import datetime
import math


def process(start:int,end:int):
    pos: int = start
    fator: int = 10000 * 10000

    while pos < end:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":

    now = datetime.datetime.now()
    process(1,1000)
    finish = datetime.datetime.now() - now
    print(f'Time to finish Python {finish}')

"""
Result
Time to finish Python 0:00:00.000243
"""