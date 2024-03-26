from P2_v2 import Almacen
from P2_v2 import Funciones


def main():
    almacen = Almacen()
    funcion = Funciones()
    almacen.fromCSV("19_ucl_stats.csv")
    # Menu que muestra las opciones y evalúa la opción seleccionada
    menu = True
    while menu:
        print(" **** Menu del programa **** ", end="\n\n")
        print("1. Alta jugador")
        print("2. Baja jugador")
        print("3. Lista de jugadores")
        print("4. Filtrado por campo")
        print("5. Guardar y salir")
        opt = input("Seleccione una opción (1-5): ")
        print("\n")

        match opt:
            case "1":
                print("*----- Alta Jugador -----*", end="\n\n") 
                # Agregamos el nuevo jugador al final de la lista, tomando el campo ID como campo autoincremental
                # El ID lo calculamos por el tamaño de la lista 'jugadores' + 1
                id,jugador = funcion.validar_datos_jugador(len(almacen.jugadores) + 1)
                almacen.alta_jugador(id, jugador)
            case "2":
                print("*----- Baja Jugador -----*", end="\n\n")
                id = int(input("Introduzca el [id] del jugador: "))
                almacen.baja_jugador(id)
            case "3":
                print("*----- Lista de Jugadores -----*", end="\n\n")
                almacen.listado_jugadores()
            case "4":
                print("*----- Filtrado por Campo -----*", end="\n\n")
                almacen.agrupar_por_campo()
            case "5":
                print("*-----Guardar y salir-----*")
                almacen.toCSV("19_ucl_stats_updated.csv")
                menu = False
                print("Guardando datos ...\n" + "Adios!")
            case _:
                print("Opción no valida!", end="\n\n")
        if menu is True:
            input("Presione [Enter] para volver al menu principal  ")


if __name__ == "__main__":
    main()
