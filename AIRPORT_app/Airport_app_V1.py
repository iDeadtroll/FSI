# Implementacion basica para el 'despegue'

import threading
import time

# Constantes
NUM_PISTAS = 5
TIEMPO_DESPEGUE = 15
TIEMPO_ATERRIZAJE = 10
TIEMPO_LLEGADA_PISTA = 5
TIEMPO_ENTRE_VIP = 30

# Semáforos
pistas = [threading.Semaphore(1) for _ in range(NUM_PISTAS)]
mutex = threading.Semaphore(1)
aviones_normales = threading.Semaphore(0)
aviones_vip = threading.Semaphore(0)

# Variables globales
aviones_en_espera = {"normal": 0, "vip": 0}
ultimo_avion = None

class Avion(threading.Thread):
    def __init__(self, id, tipo):
        threading.Thread.__init__(self)
        self.id = id
        self.tipo = tipo

    def run(self):
        global ultimo_avion
        # Solicitar pista
        print(f"Avión {self.tipo.upper()} {self.id} solicita una pista para despegar.")
        mutex.acquire()
        aviones_en_espera[self.tipo] += 1
        if self.tipo == "normal" or (self.tipo == "vip" and ultimo_avion != "vip"):
            pistas[self.id].acquire()
        mutex.release()
        aviones_normales.release() if self.tipo == "normal" else aviones_vip.release()
        # Dirigirse a la pista
        print(f"Avión {self.tipo.upper()} {self.id} dirigiéndose a pista de despegue.")
        time.sleep(TIEMPO_LLEGADA_PISTA)
        # Despegar
        print(f"Avión {self.tipo.upper()} {self.id} despegando en Pista {self.id}.")
        time.sleep(TIEMPO_DESPEGUE)
        print(f"Avión {self.tipo.upper()} {self.id}, hasta luego.")
        ultimo_avion = self.tipo
        pistas[self.id].release()

def main(m, n):
    aviones = [Avion(i % NUM_PISTAS, "normal") for i in range(m)] + [Avion(i % NUM_PISTAS, "vip") for i in range(n)]
    for avion in aviones:
        avion.start()
    for avion in aviones:
        avion.join()

if __name__ == "__main__":
    main(2, 2)  # 2 aviones normales, 2 aviones VIP
