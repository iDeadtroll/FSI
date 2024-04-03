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