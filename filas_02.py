import queue
import threading
import time

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Iniiando thread %s. " % self.name)
        processando_fila()
        print("Encerrando thread %s. " % self.name)

def processando_fila():
    while True:
        try:
            x = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            fatoracao(x)
        time.sleep(3)

def fatoracao(x):
    resultado = 'Fatores positivos de %i sao: '% x
    for i in range(1, x + 1):
        if x % i == 0:
            resultado += str(i) + ' '
    resultado += '\n' + '-' * 30
    print (resultado)

my_queue = queue.LifoQueue()

numeros = [1, 10, 4, 3]

for j in numeros:
    my_queue.put(j)


for k in numeros:
    fatoracao(k)

# INSTANCIANDO NOSSAS TAREFAS
thread1= myThread('A')
thread2= myThread('B')
thread3= myThread('C')

# INICIANDO AS TAREFAS
thread1.start()
thread2.start()
thread3.start()

# FINALIZANDO AS THREADS
thread1.join()
thread2.join()
thread3.join()

print("Concluido!!")
