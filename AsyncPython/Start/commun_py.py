import datetime
import math

def main():
    inicio = datetime.datetime.now()

    computar(fim=50_000_000)

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


# Finished in 15.09