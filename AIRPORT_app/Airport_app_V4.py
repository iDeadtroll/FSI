# Implementacion basica para el 'despegue' y 'aterrizaje' y asignacion de pistas aleatoriamente
# Agregar mensajes para mostrar el estado de los aviones

import threading
import random
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
    def __init__(self, id, tipo, estado):
        threading.Thread.__init__(self)
        self.id = id
        self.tipo = tipo
        self.estado = estado  # "aire" o "tierra"

    def run(self):
        global ultimo_avion
        operacion = "aterrizar" if self.estado == "aire" else "despegar"
        print(f"Avión {self.tipo.upper()} {self.id} está en {self.estado}.")
        print(f"Avión {self.tipo.upper()} {self.id} solicita una pista para {operacion}.")
        mutex.acquire()
        aviones_en_espera[self.tipo] += 1
        if self.tipo == "normal" or (self.tipo == "vip" and ultimo_avion != "vip"):
            pista_asignada = random.randint(0, NUM_PISTAS - 1)  # Asignación aleatoria de pista
            print(f"Pista {pista_asignada} preparada.")
            pistas[pista_asignada].acquire()
            print(f"Pista {pista_asignada} asignada a Avión {self.tipo.upper()} {self.id}.")
        mutex.release()
        aviones_normales.release() if self.tipo == "normal" else aviones_vip.release()
        print(f"Avión {self.tipo.upper()} {self.id} dirigiéndose a pista de {operacion}.")
        time.sleep(TIEMPO_LLEGADA_PISTA)
        print(f"Avión {self.tipo.upper()} {self.id} {operacion} en Pista {pista_asignada}.")
        time.sleep(TIEMPO_ATERRIZAJE if operacion == "aterrizar" else TIEMPO_DESPEGUE)
        if operacion == "aterrizar":
            print(f"Avión {self.tipo.upper()} {self.id} dirigiéndose a puerta de embarque.")
        print(f"Avión {self.tipo.upper()} {self.id}, hasta luego.")
        ultimo_avion = self.tipo
        pistas[pista_asignada].release()

def main(m, n):
    aviones = [Avion(i % NUM_PISTAS, "normal", "tierra") for i in range(m)] + [Avion(i % NUM_PISTAS, "vip", "aire") for i in range(n)]
    for avion in aviones:
        avion.start()
    for avion in aviones:
        avion.join()

if __name__ == "__main__":
    main(5, 5)  # 2 aviones normales en tierra, 2 aviones VIP en el aire
