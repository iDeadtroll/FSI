# Escriba una unica sentencia (sin bucles) que permita almacenar en la variable 'res'
# una lista con los elemento menores que el entrero 'n' que se encuentren en la lista
# 'x' de numeros enteros

# Suponemos que tenemos:
x = [5,9,6,2,5,9,4,6,8,3,6,2,7,89,3,6,7,3,8,9,4,43,357,78,2,3]
n = 10

# Solucion:
res = list(filter(lambda y: y<n, x))


# Comprobamos la solucion:
print(res)