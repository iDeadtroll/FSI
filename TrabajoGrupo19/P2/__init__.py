from P2_v2 import Almacen
from P2_v2 import Funciones


def main():
    almacen = Almacen()
    funcion = Funciones()
    almacen.fromCSV("/home/developer/proyectos/FSI/TrabajoGrupo19/P2/19_ucl_stats.csv")
    # Menu que muestra las opciones y evalua la opcion seleccionada
    menu = True
    while menu:
        print(" **** Menu del programa **** ", end="\n\n")
        print("1. Alta jugador")
        print("2. Baja jugador")
        print("3. Lista de jugadores")
        print("4. Filtrado por campo")
        print("5. Guardar y salir")
        opt = input("Seleccione una opcion (1-5): ")
        print("\n")

        match opt:
            case "1":
                print("*----- Alta Jugador -----*", end="\n\n") 
                # Agregamos el nuevo jugador al final de la lista, tomando el campo ID como campo autoincremental
                # El ID lo calculamos por el tamaño del la lista 'jugadores' + 1
                id,jugador = funcion.validar_datosJugador(len(almacen.jugadores) + 1)
                almacen.altaJugador(id,jugador)
            case "2":
                print("*----- Baja Jugador -----*", end="\n\n")
                id = int(input("Introduzca el [id] del jugador: "))
                almacen.bajaJugador(id)
            case "3":
                print("*----- Lista de Jugadores -----*", end="\n\n")
                almacen.listadoJugadores()
            case "4":
                print("*----- Filtrado por Campo -----*", end="\n\n")
                almacen.agruparPorCampo()
            case "5":
                print("*-----Guardar y salir-----*")
                almacen.toCSV("/home/developer/proyectos/FSI/TrabajoGrupo19/P2/19_ucl_stats_updated.csv")
                menu = False
                print("Guardando datos ...\n" + "Adios!")
            case _:
                print("Opcion no valida!", end="\n\n")
        if menu is True:
            input("Presione [Enter] para volver al menu principal  ")


if __name__ == "__main__":
    main()
