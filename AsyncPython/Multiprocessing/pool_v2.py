from audioop import mul
import multiprocessing

def quadrado(n):
    return n ** 2

def print_process_name():
    print(f'Starting process {multiprocessing.current_process().name}')

def main():
    pool_size = multiprocessing.cpu_count() * 2

    print(f'Pool size {pool_size}')

    pool = multiprocessing.Pool(pool_size,initializer=print_process_name)

    inp = list(range(45))
    out = pool.map(quadrado,inp)

    print(f'Output: {out}')

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()