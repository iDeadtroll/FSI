# Funciones (conceptos avanzadas)


class Clase:

    def __init__(self):

        self.x = 15

    def funcion(entero, bool, lista, tupla, objeto):
        entero = 5
        bool = True
        lista[0] = "Pepe"
        lista.append(10)
        tupla = (1, 2)
        objeto.x = 10

    e = 1
    b = False
    l = [4, 6]
    t = (3, 4, 5)
    o = Clase()

    print("Before: ", e, b, l, t, o.x)
    funcion(e, b, l, t, o)
    print("After: ", e, b, l, t, o.x)


# Calcular la desviacion estandar
# Metod1

import math
import statistics as stat


def sd(*args):  # Numero variable de parametros

    m = stat.mean(args)
    r = 0
    for x in args:

        r += (x - m) ** 2

    r /= len(args)
    return math.sqrt(r)


res = sd(1, 2, 3)
print(res)

# Calcular la desviacion estandar
# Metod2 por comprehension de listas

import math
import statistics as stat


# Probar ha implementar con 'funcion generador'
def sd(*args):

    m = stat.mean(args)
    r = stat.mean([(x - m) ** 2 for x in args])
    return math.sqrt(r)


res = sd(1, 2, 3)
print(res)


# Numero variable de parametros variabe pasados como diccionarios
def example_fun(x, y, **other):  # El diccionario lo interpreta si entan al final

    print("x: {0}, y: {1}, keys in 'other': {2}".format(x, y, list(other.keys())))
    other_total = 0
    for k in other.keys():
        other_total = other_total + other[k]
    print("The total of values in 'other' is {0}".format(other_total))


example_fun(y="1", x=2, foo=3, bar=4)

# Variable que puede contener una funcion


def f_to_kelvin(degrees_f):
    return 273.15 + (degrees_f - 32) * 5 / 9


def c_to_kelvin(degrees_c):
    return 273.15 + degrees_c


abs_temperature = f_to_kelvin
abs_temperature(32)


# Funciones Lambda 'funciones anonimas'

temp_funcs = {
    "FtoK": lambda deg_f: 273.15
    + (deg_f - 32)
    * 5
    / 9,  # Probar a usar Lambda con el resultado de comprehension de listas
    "CtoK": lambda deg_c: 273.15 + deg_c,
}

temp_funcs["FtoK"](32)  # Llamamos a la funcion con el parametro (32)

# Decoradores
# Para medir el tiempo de ejecutar una funcion usando Decorador

# Metod 1

from time import time


def execution_time(f):  # funcion decoradora
    def temp(*args):
        start = time()
        res = f(*args)
        print("Execution time: ", time() - start, " secs.")

        return res

    return temp


def func(n):
    s = 0
    for i in range(1, n):

        s += i**2

    return s


r = execution_time(func)(10000000)


print("Result: ", r)

# Metod 2

from time import time


def execution_time(f):  # funcion decoradora
    def temp(*args):  # Aqui preparamos a la funcion para recibir varios parametros
        start = time()
        res = f(
            *args
        )  # *args implica desempaquetar la lista de parametros y las pasa por separado
        print("Execution time: ", time() - start, " secs.")

        return res

    return temp


@execution_time
def func(n):  # Funcion decorada
    s = 0
    for i in range(1, n):

        s += i**2

    return s


r = func(10000000)


print("Result: ", r)

# Funciones 'map', 'filter'  y 'reduce'

# map(funcion, collection)
# map es como la version reducida de comprehension de listas
# Ejemplo 1: metod 1

import math


def area(r):

    return math.pi * (r**2)


radii = [2, 5, 7.1, 0.3, 10]
areas = []
for r in radii:
    a = area(r)
areas.append(a)

print(areas)

# Ejemplo 1: metod 2

import math


def area(r):

    return math.pi * (r**2)


radii = [2, 5, 7.1, 0.3, 10]
areas = map(area, radii)  # map devuelve un objeto generador
# print(areas)
# >>> <map object at 0x7f8f482b2d90>
print(list(areas))

# Ejemplo 2:


temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19)]

c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)

print(list(map(c_to_f, temps)))
