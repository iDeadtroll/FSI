l1 = [1,2,3,-1,4]
l2 = ["H","O","L","A","!","?"]
# zip() empaqueta un objeto iterador con un numero de elementos igual al de la coleccion de menor tamaño
# Guardamos el iterador resultante de zip() para  volverlo a utilizar mas adelante
l_aux = list(zip(l2,l1)) # En este caso l_aux es una lista de tuplas.
# Lista por comprension que desempaqueta l_aux y devuelve el producto de los elementos de cada tupla.
l3 =[c * num for c, num in l_aux ]
print(l_aux)
print(l3)
# Lista por comprension que desempaqueta l_aux y devuelve el producto de los elementos de cada tupla, si 'num' es mayor que 0
l4 =[c * num for c, num in l_aux if num > 0]
print(l4)



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Cuadrados de una lista de números: Dada una lista de números, escribe un programa que devuelva una nueva lista que contenga el cuadrado de cada número.
lista_cuadrados = [n*n for n in numeros]
print("Lista cuadrados: \n" , lista_cuadrados)
# Filtrar números pares de una lista: Dada una lista de números, escribe un programa que devuelva una nueva lista que contenga solo los números pares.
lista_pares = [n for n in numeros if n % 2 == 0]
print(lista_pares)


palabras = ['hola', 'mundo', 'python', 'comprension', 'de', 'listas']
# Convertir una lista de palabras a mayúsculas: Dada una lista de palabras, escribe un programa que devuelva una nueva lista que contenga todas las palabras convertidas a mayúsculas.
lista_mayusculas = [ n.upper() for n in palabras]
print(lista_mayusculas)


lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']
# Crear una lista de tuplas a partir de dos listas: Dadas dos listas de igual longitud, escribe
# un programa que devuelva una nueva lista que contenga tuplas. Cada tupla debe contener un elemento de
# cada una de las listas originales que ocupan la misma posición.

lista_tuplas = [(c,n) for c,n in zip(lista1,lista2)]
print(lista_tuplas)

#--------------------------------------------------------------------------------------------------
# Uso de map()

cadena = "ejercicio cuatro para separa por espacios"
# Longitud de las palabras dentro de 'cadena'
def longitudes_palabras(cadena):
    palabras = cadena.split(" ")
    longitudes = list(map(len, palabras))
    return longitudes

print(longitudes_palabras(cadena))

#--------------------------------------------------------------------------------------------------
# Uso de filter()
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