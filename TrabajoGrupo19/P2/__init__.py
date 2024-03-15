from P2 import Almacen
def data_loader(ruta):
    # 'Alamacen.fromCSV() usa el patron Singleton llamando a la unica instancia Almacen'
    Almacen.fromCSV(ruta)

def main():
    data_loader("/home/developer/proyectos/FSI/TrabajoGrupo19/P2/19_ucl_stats.csv")
if __name__ == "__main__":
    main()