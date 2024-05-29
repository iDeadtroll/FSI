# Programacion Funcional

# Iteraciones y comprenhension de listas/diccionarios
# Sumar el producto de las tuplas
# Metodo 1
lista = [(1, 2), (3, 7), (9, 5)]

result = 0

for t in lista:
    result = result + (t[0] * t[1])

print(result)

# Metodo 2

lista = [(1, 2, 3), (3, 7, 3), (9, 5, 4)]

result = 0

for x, y, z in lista:
    result = result + (x * y * z)

print(result)

# Buscar valores negativos y mostrar sus indices

# Metod 1

x = [1, 3, -7, 4, 9, -5, 4]

for i in range(0, len(x)):
    if x[i] < 0:
        print(i, " ")

# Metod 2

x = [1, 3, -7, 4, 9, -5, 4]

for i, n in enumerate(x):
    if n < 0:
        print(i, " ")

# Combinar elementos

x = [1, 2, 3, 4]
y = ["a", "b", "c"]
z = zip(x, y)
print(list(z))

# Generar una lista con los cudrados de otra lista

# Metod 1
x = [1, 2, 3, 4]

x_squared = []

for item in x:
    x_squared.append(item**2)
print(x_squared)

# Medot 2

x = [1, 2, 3, 4]

x_squared = [item**2 for item in x]

print(x_squared)

# Generar una lista con los cudrados de otra lista usando solo los indices pares

# Medot 1

x = [1, 2, 3, 4]

x_squared = []

for item in x:
    if item % 2 == 0:
        x_squared.append(item**2)

# Metod 2

x = [1, 2, 3, 4]

x_squared = [item**2 for item in x if item % 2 == 0]

# Los mismo pero para diccionarios

# dic = {key : value for variable in collection if condition}

# Medot 1

names = ["John", "Charles"]
salaries = [1500, 2000]

dic = {}
for i in range(0, len(names)):
    dic[names[i]] = salaries[i]

print(dic)
# Metod 2

names = ["John", "Charles"]
salaries = [1500, 2000]

dic = {x[0]: x[1] for x in zip(names, salaries)}

print(dic)


# Gneradores
# Es un objeto capaz de crear una lista pero las crea hasta que sea necesario(es decir cuando se llame a la fucnion generadora)


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
