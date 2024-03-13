# Usamos import csv para leer el dataset.
import csv

diccionario1 = dict()
id_registros = []
encabezado = ()

# TODO: probar a leer el dataset sin libreria "csv"
with open("/home/developer/proyectos/FSI/TrabajoGrupo19/P1/19_ucl_stats.csv", "r", encoding="utf-8") as archivo:
    contenido = csv.reader(archivo, delimiter=",")
    # Guardamos la primera linea en "encabezado"
    encabezado = next(contenido)

    # Empesamos a leer el contenido desde la segunda linea
    # Recorrido para construir el diccionario y la lista de IDs de cada registro.
    for linea in contenido:
        valor = tuple(linea)
        id_registros.append(valor[0])
        clave = valor[0]
        diccionario1[clave] = valor


def nuevo_registro():
    # Nuevo registro generado a partir de los campos de la tupla encabezado. 
    # Tupla que hace referencia a los indices del encabezado del dataset.
    print("Introduzca nuevo registro")

    # "nuevo_registro" contendrá el mismo numero de elementos que "encabezado"
    nuevo_registro = []
    i = 0
    #   Bucle añade los campos necesarios para el nuevo registro.
    while len(nuevo_registro) < len(encabezado):
        nuevo_elemento = str(input("Introduzca " + encabezado[i] + ": "))
        nuevo_registro.append(nuevo_elemento)
        i = i + 1

    # La nueva_tupla será el valor del nuevo item del diccionario.
    nueva_tupla = tuple(nuevo_registro)

    # TODO: Probar este misma funcion usan la funcion get() y la opcion por defecto.
    # Evaluar si el nuevo registro existe, caso contrario se agrega el nuevo registro al diccionario.
    if nueva_tupla[0] not in diccionario1:
        diccionario1[(nueva_tupla[0])] = nueva_tupla
        print(diccionario1.get(nueva_tupla[0]))
    else:
        print("El registro ", nueva_tupla[0], " ya existe. Intente con otro numero de registro.")




def tabla_diccionario():
    # TODO: mostrar un formato de tabla con los tamanios de los campos fijos
    for k, v in diccionario1.items():
        print("    |   ".join(map(str, v)))


def borrar_registro():
    # Mostramos los 10 primeros
    for i in range(1,10):
        print(diccionario1.get(str(i)))
    # TODO: vefificar que el registro existe y pedir confirmacion para eliminarlo

    reg = str(input("Introduce el ID del registro: "))
    diccionario1.pop(reg)

    # TODO: mostrar el ID del registro que se ha aliminado e indicar que se ha realizado correctamente.

    # Mostramos los 10 primeros y verificamos que se ha eliminado
    for i in range(1,10):
        print(diccionario1.get(str(i)))


def busca_clave_mostrar_valor():

    # TODO: vefificar que el registro existe, caso contrario pedir nuevamente el ID
    reg = str(input("Introduce el ID del registro: "))
    
    print(diccionario1.get(reg))


def mostrarOpciones():
    print(" **** Menu del programa **** ", end="\n\n")
    print("1. Agregar un nuevo registro")
    print("2. Buscar un registro por su clave y mostrar sus valores")
    print("3. Borrar un registro a partir de su clave")
    print("4. Listar todos los registros en formato de tabla")
    print("5. Salir")



# Menu que muestra las opciones y evalua la opcion seleccionada
s = True
while s:
    mostrarOpciones()
    opt = input("Seleccione una opcion (1-5): ")
    print("\n")

    match opt:
        case "1":
            print("Opcion: Agregar nuevo registro", end="\n\n")
            nuevo_registro()
        case "2":
            print("Opcion: Buscar un registro por su clave y mostrar sus valores", end="\n\n")
            busca_clave_mostrar_valor()
        case "3":
            print("Borrar un registro a partir de su clave", end="\n\n")
            borrar_registro()
        case "4":
            print("Listar todos los registros en formato de tabla", end="\n\n")
            tabla_diccionario()
        case "5":
            s = False
            print("Adios")
        case _:
            print("Opcion no valida!", end="\n\n")
    if s is True:
        input("Precione una tecla para volver al menu")
