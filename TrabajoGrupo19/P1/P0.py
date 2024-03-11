# Abre el archivo
f = open("19_ucl_stats.csv", "r")
# Lee el contenido del archivo
contenido = f.read().splitlines()

# Elimina la primera línea (encabezado)
contenido = contenido[1:]

# Inicializa el diccionario y la lista
diccionario1 = dict()
lista_nums_registros = list()

# Recorre cada línea del contenido
for linea in contenido:
    # Divide la línea por comas
    tupla_valor = tuple(linea.split(","))

    # Agrega el primer valor a la lista
    lista_nums_registros.append(tupla_valor[0])

    # Crea una clave con el primer y último valor
    tupla_clave = (tupla_valor[0], tupla_valor[-1])

    # Agrega la tupla al diccionario
    diccionario1[tupla_clave] = tupla_valor

print(lista_nums_registros)
