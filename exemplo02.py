from math import sqrt
import concurrent.futures
from timeit import default_timer as timer

def f(x):
    return x**2 - x + 1

def concorrente_f(i):
    global result
    result = f(result)


def main():

    # Sequencial
    start = timer()
    result_seq = 3
    for _ in range(20):
        result_seq = f(result_seq)

    print("[Sequencial]. Ultimos 5 digitos:", result_seq % 100000)
    print("[Sequencial] Tempo: %.4f segundos\n" % (timer() - start))


    # Concorrente

    global result
    result = 3
    start = timer()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(concorrente_f, i) for i in range(20)]
        concurrent.futures.wait(futures)

    print("[Concorrente] Ultimos 5 digitos:", result % 100000)
    print("[Concorrente] Tempo: %.4f segundos." % (timer() - start))

if __name__ == "__main__":
    main()
