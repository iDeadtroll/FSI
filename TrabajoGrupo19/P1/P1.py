# Usamos import csv para leer el dataset.
import csv

diccionario1 = dict()
encabezado = ()

def data_extractor():
    global encabezado

    # TODO: probar a leer el dataset sin libreria "csv"
    with open("/home/developer/proyectos/FSI/TrabajoGrupo19/P1/19_ucl_stats.csv", "r", encoding="utf-8") as archivo:
        contenido = csv.reader(archivo, delimiter=",")
        # Asignamos la primera linea a la tupla "encabezado"
        encabezado = next(contenido)

        # Empesamos a leer el contenido desde la segunda linea
        # Bucle para construir el diccionario tomando como clave el primer campo de cada linea.
        for linea in contenido:
            valor = tuple(linea)
            clave = valor[0]
            diccionario1[clave] = valor
    


def nuevo_registro():
    # Nuevo registro generado a partir de los campos de la tupla encabezado. 
    # Tupla que hace referencia a los indices del encabezado del dataset.
    print("Introduzca nuevo registro:")

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

    # Evaluar si el nuevo no registro existe, caso contrario no se agregara el nuevo registro al diccionario.
    if nueva_tupla[0] not in diccionario1:
        diccionario1[(nueva_tupla[0])] = nueva_tupla
        print("\nEl registro :" + str(diccionario1.get(nueva_tupla[0])) + "\n Ha sido hagregado correctamente!\n")
    else:
        print("El registro con ID [" + nueva_tupla[0] + "] ya existe. Intente con otro valor de registro.")



def tabla_diccionario():
    # Mostrar un formato de tabla con los tamaños de los campos fijos de la cabecera
    print("{:<10} {:<26} {:<12} {:<10} {:<20} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<8} {:<8} {:<8} {:<8}\n".format(*encabezado))
    # Mostrar un formato de tabla con los tamaños de los campos fijos del resto de filas
    for v in diccionario1.values():
            print("{:<10} {:<26} {:<12} {:<10} {:<20} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<8} {:<8} {:<8} {:<8}".format(*v))



def borrar_registro():
    # Mostramos los 10 primeros
    for i in range(1,10):
        print(diccionario1.get(str(i)))

    # Vefificar que el registro existe y pedir confirmacion antes de eliminarlo
    reg = str(input("Introduce el ID del registro: "))
    while reg not in diccionario1.keys():
        print("ID no exite!")
        reg = str(input("Introduce el ID del registro: "))
    print("¿Desea eliminar el registro: " + reg + " ?")
    confirmar = str.upper(input("Presione[S] para confirmar: "))
    
    # Si el registro existe en el diccionario y se confirma la accion
    if reg in diccionario1.keys() and confirmar == "S": 
        diccionario1.pop(reg)
        print("Registro" +"[" + reg + "]" + "eliminado correctamente!\n")
    else:
        print(("Registro" +"[" + reg + "]" + "no eliminado!\n"))

    # Mostramos los 10 primeros y verificamos que se ha eliminado
    for i in range(1,10):
        print(diccionario1.get(str(i)))


def buscaClave_mostrarValor():

    # Vefificar que el registro existe, caso contrario pedir nuevamente el ID
    
    reg = str(input("Introduce el ID del registro: "))
    while reg not in diccionario1.keys():
        print("ID no exite!")
        reg = str(input("Introduce el ID del registro: "))
    # Mostrar datos de la tupla correspondiente al registro
    if reg in diccionario1.keys():
        d = diccionario1.get(reg)
        print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*encabezado))
        print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*d))
    return reg

def buscarEditar_mostrar():

    reg = buscaClave_mostrarValor()
    print("Desea editar el registro?")
    editar=str.upper(input("Presion [S] para confirmar: "))
    if editar=="S":
        nuevo_registro = [reg]
        i = 1
        #   Bucle añade los campos necesarios para el nuevo registro.
        while len(nuevo_registro) < len(encabezado):
            nuevo_elemento = str(input("Introduzca " + encabezado[i] + ": "))
            nuevo_registro.append(nuevo_elemento)
            i = i + 1

        # nueva_tupla será el valor que remplazara al valor actual del registro.
        nueva_tupla = tuple(nuevo_registro)
        diccionario1[reg] = nueva_tupla
        d = diccionario1.get(reg)
        print("\nEl registro " + str(nuevo_registro[0] + " ha sido modificado:\n"))
        print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*encabezado))
        print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*d))

        

    


def mostrarOpciones():
    print(" **** Menu del programa **** ", end="\n\n")
    print("1. Agregar un nuevo registro")
    print("2. Buscar un registro por su clave y mostrar sus valores")
    print("3. Buscar un registro por su clave, editarlo y mostrar sus valores")
    print("4. Borrar un registro a partir de su clave")
    print("5. Listar todos los registros en formato de tabla")
    print("6. Salir")


def menu_principal():
# Menu que muestra las opciones y evalua la opcion seleccionada
    s = True
    while s:
        mostrarOpciones()
        opt = input("Seleccione una opcion (1-5): ")
        print("\n")

        match opt:
            case "1":
                print("Opcion 1", end="\n\n")
                nuevo_registro()
            case "2":
                print("Opcion 2", end="\n\n")
                buscaClave_mostrarValor()
            case "3":
                print("Opcion 3", end="\n\n")
                buscarEditar_mostrar()
            case "4":
                print("Opcion 4", end="\n\n")
                borrar_registro()
            case "5":
                print("Opcion 5", end="\n\n")
                tabla_diccionario()
            case "6":
                s = False
                print("Adios")
            case _:
                print("Opcion no valida!", end="\n\n")
        if s is True:
            input("Presione [Enter] para volver al menu principal  ")
