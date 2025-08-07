from math import sqrt
import concurrent.futures
from timeit import default_timer as timer

def eh_primo(n1):
    if n1 < 2:
        return False

    if n1 == 2:
        return n1

    if n1 % 2 == 0:
        return False

    limit = int(sqrt(n1)) + 1
    for i in range(3, limit, 2):
        if n1 % i == 0:
            return False

    return n1

def main():
    numeros = [i for i in range(10 ** 13, 10 ** 13 + 500)]

    # Sequencial
    start = timer()
    result = [i for i in numeros if eh_primo(i)]
    print("Resultado Seq:", result)
    print("EndTime: %.4f segundos. " % (timer() - start))


# Concorrente

    start = timer()
    result = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for r in executor.map(eh_primo, numeros):
            if r:
                result.append(r)


    print("Resultado Concorrente:", result)
    print("EndTime: %.4f segundos. " % (timer() - start))

if __name__ == "__main__":
    main()
