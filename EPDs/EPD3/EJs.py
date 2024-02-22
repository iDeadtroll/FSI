# Ejercicio 1


def decrementar(n):
    n = n - 1

    return n


def cuentaAtras(n):
    yield decrementar(n)


a = cuentaAtras(10)
print(next(a))

# Ejercicio 2

import random


def sucesos(probabilidad):
    while True:
        yield random.random() < probabilidad


# Crear un generador con una probabilidad de 0.5
generador = sucesos(0.5)

# Imprimir los primeros 10 valores
for _ in range(10):
    print(next(generador))


# Ejercicio 3


multiplos_de_tres = [i for i in range(1, 101) if i % 3 == 0]

print(multiplos_de_tres)

# Ejercicio 4: Metodo 1

cadena = "ejercicio cuatro para separa por espacios"


def longitudes_palabras(cadena):
    palabras = cadena.split(" ")
    longitudes = list(map(len, palabras))
    return longitudes


print(longitudes_palabras(cadena))

# Ejericio 5
# Dado el diccionario de datos de ejemplo, realice las operaciones que se piden utilizando funciones de orden
# superior (filter, map, reduce), funciones lambda y comprensión de listas. Cualquier solución que utilice bucles no se
# considerará válida. Se pueden dar soluciones utilizando resultados (listas, generadores, tuplas, ...) auxiliares o intermedios.


# a) Escriba una función obtenerPasajeros(diccionario), que tomando como parámetro de entrada el diccionario anterior,
# devuelva una tupla con los pasajeros de cada ferry.

diccionario = {
    ("ferry", 1): [2500, 350],  # [ carga, pasajeros ]
    ("mercante", 2): [120000, 6500],  # [ carga, autonomía ]
    ("mercante", 3): [200000, 3200],  # [ carga, autonomía ]
    ("ferry", 4): [3520, 420],  # [ carga, pasajeros ]
}


def obtenerPasajeros(diccionario):

    # Filtrar los ferries
    ferries = filter(lambda x: x[0][0] == "ferry", diccionario.items())

    # Obtener los pasajeros de cada ferry
    pasajeros = map(lambda x: x[1][1], ferries)

    # Devolver los pasajeros como una tupla
    return tuple(pasajeros)


print(obtenerPasajeros(diccionario))


diccionario = {
    ("ferry", 1): [2500, 350],  # [ carga, pasajeros ]
    ("mercante", 2): [120000, 6500],  # [ carga, autonomía ]
    ("mercante", 3): [200000, 3200],  # [ carga, autonomía ]
    ("ferry", 4): [3520, 420],  # [ carga, pasajeros ]
}


def obtenerCarga(diccionario):
    mercantes = filter(lambda x: x[0][0] == "mercante", diccionario.items())

    carga = map(lambda x: x[1][1], mercantes)

    return list(carga)


print(obtenerCarga(diccionario))
