import threading
import time
import random

semaphore = threading.Semaphore(0)

def consumidor():
    print('Consumidor esta aguardando')
    semaphore.acquire()
    print('Consmidor notificado:')
    print('consumindo item numero %s ' % item)

def produtor():
    global item
    time.sleep(10)
    item = random.randint(0, 1000)
    print('Produtor notificando:')
    print('produzinho item numero %s ' % item)

    semaphore.release()

if __name__== '__main__':
    for i in range(0, 5):
        t1 = threading.Thread(target=produtor)
        t2 = threading.Thread(target=consumidor)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print('Programa encerrado!!')
