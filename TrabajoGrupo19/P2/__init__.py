from P2_v2 import Almacen
from P2_v2 import Funciones




def main():
    almacen = Almacen()
    funcion = Funciones()
    almacen.fromCSV("/home/developer/proyectos/FSI/TrabajoGrupo19/P2/19_ucl_stats.csv")
    # Menu que muestra las opciones y evalua la opcion seleccionada
    s = True
    while s:
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
                print("Opcion 1", end="\n\n")
                almacen.jugadores
                jugador = funcion.validar_datosJugador()
                almacen.altaJugador(jugador)
            case "2":
                print("Opcion 2", end="\n\n")
                id = int(input("Introduzca el id del jugador: "))
                almacen.bajaJugador(id)
            case "3":
                print("Opcion 3", end="\n\n")
                almacen.listadoJugadores()
            case "4":
                print("Opcion 4", end="\n\n")
                almacen.agruparPorCampo()
            case "5":
                almacen.toCSV("/home/developer/proyectos/FSI/TrabajoGrupo19/P2/19_ucl_stats_updated.csv")
                s = False
                print("Adios")
            case _:
                print("Opcion no valida!", end="\n\n")
        if s is True:
            input("Presione [Enter] para volver al menu principal  ")


if __name__ == "__main__":
    main()
