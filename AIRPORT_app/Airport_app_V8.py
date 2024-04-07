# Implementacion basica para el 'despegue' y 'aterrizaje' y asignacion de pistas aleatoriamente
# Agregar mensajes para mostrar el estado de los aviones
# Asignacion del estado aterrizar o despegar de forma aletoria
# Arreglado el fallo en asignacion aleatoria de pista
# Arreglo de la condicion para que dos vips operen de forma consecutiva, si hay aviones normales esperando.
# Arreglo para ID del avion y como se muestra por consola.
# Arreglo para mostrar el estado inicial de los aviones antes de soli

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
ultimo_vip = 0  # Tiempo en el que el último avión VIP despegó o aterrizó

class Avion(threading.Thread):
    def __init__(self, id, tipo, estado):
        threading.Thread.__init__(self)
        self.id = id
        self.tipo = tipo
        self.estado = estado  # "aire" o "tierra"
        self.operacion = "aterrizar" if estado == "aire" else "despegar"  # Operación basada en el estado

    def run(self):
        global ultimo_avion, ultimo_vip
        print(f"Avión [{self.id}] {self.tipo.upper()} está en {self.estado}, esperando para {self.operacion}.")
        mutex.acquire()
        aviones_en_espera[self.tipo] += 1
        pista_asignada = random.randint(0, NUM_PISTAS - 1)  # Asignación aleatoria de pista
        if self.tipo == "normal" or (self.tipo == "vip" and ultimo_avion != "vip"):
            print(f"Pista {pista_asignada} preparada.")
            pistas[pista_asignada].acquire()
            print(f"Pista {pista_asignada} asignada a Avión [{self.id}] {self.tipo.upper()}.")
            if self.tipo == "vip":
                ahora = time.time()
                if ultimo_avion == "vip" and ahora - ultimo_vip < TIEMPO_ENTRE_VIP:
                    time.sleep(TIEMPO_ENTRE_VIP - (ahora - ultimo_vip))
                ultimo_vip = time.time()
        mutex.release()
        aviones_normales.release() if self.tipo == "normal" else aviones_vip.release()
        print(f"Avión [{self.id}] {self.tipo.upper()} dirigiéndose a pista de {self.operacion}.")
        time.sleep(TIEMPO_LLEGADA_PISTA)
        print(f"Avión [{self.id}] {self.tipo.upper()} {self.operacion} en Pista {pista_asignada}.")
        time.sleep(TIEMPO_ATERRIZAJE if self.operacion == "aterrizar" else TIEMPO_DESPEGUE)
        if self.operacion == "aterrizar":
            print(f"Avión [{self.id}] {self.tipo.upper()} dirigiéndose a puerta de embarque.")
        print(f"Avión [{self.id}] {self.tipo.upper()}, hasta luego.")
        ultimo_avion = self.tipo
        pistas[pista_asignada].release()

def main(m, n):
    aviones = [Avion(i, "normal", "tierra") for i in range(m)] + [Avion(i + m, "vip", "aire") for i in range(n)]
    for avion in aviones:
        avion.start()
    for avion in aviones:
        avion.join()

if __name__ == "__main__":
    main(6, 4)  # 6 aviones normales en tierra, 4 aviones VIP en el aire