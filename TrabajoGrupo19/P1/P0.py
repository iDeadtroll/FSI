datos = dict()
datos[0] = "Jonathan"
print(datos)


# Usamos import csv para leer el dataset.
import csv

diccionario1 = dict()
id_registros = []
encabezado = []

with open("/home/developer/proyectos/FSI/TrabajoGrupo19/P1/19_ucl_stats.csv", "r", encoding="utf-8") as archivo:
    contenido = csv.reader(archivo, delimiter=",")
    
    encabezado = next(contenido)

    # Empesamos a leer el contenido desde la segunda linea
    next(contenido, None)
    #   Recorrido para construir el diccionario y la lista de IDs de cada registro.
    for linea in contenido:
        valor = tuple(linea)
        id_registros.append(valor[0])
        clave = valor[0]
        diccionario1[clave] = valor
        
