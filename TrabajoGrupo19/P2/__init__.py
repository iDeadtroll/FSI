from P2 import Almacen

def main():
    
    jugadores, cabecera = Almacen.fromCSV("/home/developer/proyectos/FSI/TrabajoGrupo19/P2/19_ucl_stats.csv")
    print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*cabecera))
    for j in jugadores:
        print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*j))

if __name__ == "__main__":
    main()