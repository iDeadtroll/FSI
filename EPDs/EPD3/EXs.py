# Experimento 1


def cuadrado(n):
    return n**2


l = [1, 2, 3]
l2 = map(cuadrado, l)

# Experiemento 2

from functools import reduce


def cuadrado(n):
    return n**2


l = [1, 2, 3]
l2 = reduce(
    lambda s, x: s + cuadrado(x), l
)  # El primer parametro es la funcion Lambda y el segundo es la coleccion
print(l2)

# Experimento 3: comparar el siguiente codigo con el de Experiento 1

l = [1, 2, 3]
l2 = [n**2 for n in l]

# Experiento 4:

l = [1, 2, 3]
l2 = (n**2 for n in l)


# Experimento 5:


def generador():
    yield 5


print(generador())  # imprime un object de tipo generador

# Experimento 6:


def generador():
    yield 5


a = generador()
print(next(a))
print(next(a))

# Experimento 7:


def generador():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n


for i in generador():
    print(i)

# Experimento 8

x = lambda a, b: (b + 1, a + 1)
print(x(3, 9))
