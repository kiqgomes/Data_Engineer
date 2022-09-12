import multiprocessing

print(f"Starting multiprocessing {multiprocessing.current_process().name}")

def faz_Algo(algo):
    print(f'Algum {algo}')

def main():

    print('Creating the new process...')

    pc = multiprocessing.Process(target=faz_Algo,args=("item",),name='Fucking Process')

    print(f'Starting process {pc.name}')

    pc.start()
    pc.join()

if __name__ == '__main__':
    main()