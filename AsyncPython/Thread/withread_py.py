from audioop import mul
import datetime
import math
from threading import Thread
import multiprocessing

def main():
    cores = multiprocessing.cpu_count()
    print(f'Utilizando {cores} cores para essa tarefa')

    inicio = datetime.datetime.now()


    threads = []
    for c in range(1,cores + 1):
        
        ini = 50_000_000 * (c - 1)/cores
        fim = 50_000_000 * c / cores

        print(f'Core {c} processando de {ini} até {fim}')
        
        threads.append(
            Thread(
                target=computar
                ,kwargs={'inicio':ini
                        ,'fim':fim}
                ,daemon=True
            )
        )

    [th.start() for th in threads]
    [th.join() for th in threads]

    tempo = datetime.datetime.now() - inicio

    print(f'Finished in {tempo.total_seconds():.2f}')

def computar(fim,inicio=1):

    posicao = inicio
    fator = 1000 * 1000
    while posicao < fim:
        posicao+=1
        math.sqrt((posicao - fator) * (posicao - fator))




if __name__ == '__main__':
    main()


# Finished in 10.43