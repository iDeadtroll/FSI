# Escribir una funcion que reciba el nombre de un fichero que incluye en cada linea el nombre de una
# persona y su edad (ambos separados por un punto y coma ";"). La funcion leerá todas las lineas del 
# fichero y devolverá una lista de tuplas, cada una formada por el nombre de la persona y su edad.


# Solucion:
def funcion(nombre):
    with open(nombre) as file:
        lista = []
        for linea in file:
            campos = linea.rstrip().split(";")
            lista.append(tuple(campos))
        return lista

# Comprobamos la solucion:
nombre = "nombres.txt"    
print(funcion(nombre))