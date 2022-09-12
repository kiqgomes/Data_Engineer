from audioop import mul
import multiprocessing

def quadrado(n):
    return n ** 2

def main():
    pool_size = multiprocessing.cpu_count() * 2

    print(f'Pool size {pool_size}')

    pool = multiprocessing.Pool(pool_size)

    inp = list(range(7))
    out = pool.map(quadrado,inp)

    print(f'Output: {out}')

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()