import csv


# Clase que implementa las propiedades y metodos necesarios gestionar los objetos Jugador
class Jugador:

    # Método constructor del objeto Jugador
    def __init__(
        self,
        id: int,
        jugador: str,
        nacionalidad: str,
        posicion: str,
        club: str,
        edad: int,
        nacimiento: int,
        partidos_jugados: int,
        partidos_titular: int,
        minutos_jugados: int,
        n: float,
        goles: int,
        asistencias: int,
        G_A: int,
        G_PK: int,
        PK: int,
    ):
        self.__id = id
        self.__jugador = jugador
        self.__nacionalidad = nacionalidad
        self.__posicion = posicion
        self.__club = club
        self.__edad = edad
        self.__nacimiento = nacimiento
        self.__partidos_jugados = partidos_jugados
        self.__partidos_titular = partidos_titular
        self.__minutos_jugados = minutos_jugados
        self.__n = n
        self.__goles = goles
        self.__asistencias = asistencias
        self.__G_A = G_A
        self.__G_PK = G_PK
        self.__PK = PK

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def jugador(self):
        return self.__jugador

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @property
    def posicion(self):
        return self.__posicion

    @property
    def club(self):
        return self.__club

    @property
    def edad(self):
        return self.__edad

    @property
    def nacimiento(self):
        return self.__nacimiento

    @property
    def partidos_jugados(self):
        return self.__partidos_jugados

    @property
    def partidos_titular(self):
        return self.__partidos_titular

    @property
    def minutos_jugados(self):
        return self.__minutos_jugados

    @property
    def n(self):
        return self.__n

    @property
    def goles(self):
        return self.__goles

    @property
    def asistencias(self):
        return self.__asistencias

    @property
    def G_A(self):
        return self.__G_A

    @property
    def G_PK(self):
        return self.__G_PK

    @property
    def PK(self):
        return self.__PK

    # Setters
    @id.setter
    def id(self, id):
        self.__id = id

    @jugador.setter
    def jugador(self, jugador):
        self.__jugador = jugador

    @nacionalidad.setter
    def nacionalidad(self, nt):
        self.__nacionalidad = nt

    @posicion.setter
    def posicion(self, pos):
        self.__posicion = pos

    @club.setter
    def club(self, club):
        self.__club = club

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @nacimiento.setter
    def nacimiento(self, nac):
        self.__nacimiento = nac

    @partidos_jugados.setter
    def partidos_jugados(self, pj):
        self.__partidos_jugados = pj

    @partidos_titular.setter
    def partidos_titular(self, pt):
        self.__partidos_titular = pt

    @minutos_jugados.setter
    def minutos_jugados(self, mj):
        self.__minutos_jugados = mj

    @n.setter
    def n(self, n):
        self.__n = n

    @goles.setter
    def goles(self, goles):
        self.__goles = goles

    @asistencias.setter
    def asistencias(self, asistencias):
        self.__asistencias = asistencias

    @G_A.setter
    def G_A(self, G_A):
        self.__G_A = G_A

    @G_PK.setter
    def G_PK(self, G_PK):
        self.__G_PK = G_PK

    @PK.setter
    def PK(self, PK):
        self.__PK = PK

    # Método para imprimir las propiedades del objeto Jugador como un string
    def __str__(self):
        return f"{self.__id} {self.__jugador} {self.__nacionalidad} {self.__posicion} {self.__club} {self.__edad} {self.__nacimiento} {self.__partidos_jugados} {self.__partidos_titular} {self.__minutos_jugados} {self.__goles} {self.__asistencias} {self.__G_A} {self.__G_PK} {self.__PK}"

    # Método que toma las propiedades del objeto Jugador para construir un iterable de dicho objeto
    # Usaremos este método para mostrar los campos de cada Jugador con un formato de tabla más adelante
    def __iter__(self):
        yield self.__id
        yield self.__jugador
        yield self.__nacionalidad
        yield self.__posicion
        yield self.__club
        yield self.__edad
        yield self.__nacimiento
        yield self.__partidos_jugados
        yield self.__partidos_titular
        yield self.__minutos_jugados
        yield self.__n
        yield self.__goles
        yield self.__asistencias
        yield self.__G_A
        yield self.__G_PK
        yield self.__PK


# Clase que implementa las propiedades y metodos que permiten gestionar la lista de objetos Jugador
class Almacen:

    _instance = None  # variable de clase que se utiliza para almacenar la única instancia de Almacen
    _jugadores = list()
    _cabecera = list()

    def __init__(self):
        self._jugadores = []
        self._cabecera = []
    @property
    def jugadore(self):
        return self._jugadores

    def altaJugador(self, j: Jugador):
        self._jugadores.append(j)
        return j

    def bajaJugador(self, ID: int):
        pass

    def listadoJugadores(self):
        # 'Alamacen.fromCSV() usa el patron Singleton llamando a la unica instancia Almacen'
        jugadores, cabecera = Almacen.fromCSV(ruta)
        print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*cabecera))

        # '*j' hace referencia a un objeto iterable necesario recorrer campo a campo del objeto Jugador
        for j in jugadores:
            print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*j))



    def agruparPorCampo(self, campo: str):
        return {getattr(j, campo): j for j in self._jugadores}

    # Declaramos fromCSV()como método estático para llamar al método sin la necesidad
    # de crear una instancia de Almacen en cada llamada a dicho método
    # (necesario para implementar Patron Singleton)

    def fromCSV(ruta: str):  # Recibe la ruta del archivo como parámetro

        with open(ruta, "r") as archivo:
            contenido = csv.reader(
                archivo
            )  # Creamos un objeto contenido para despues iterar linea a linea
            cabecera = next(contenido)  # Saltamos la cabecera
            for linea in contenido:  # Recorremos contenido linea a linea
                (
                    id,
                    jugador,
                    nacionalidad,
                    posicion,
                    club,
                    edad,
                    nacimiento,
                    partidos_jugados,
                    partidos_titular,
                    minutos_jugados,
                    n,
                    goles,
                    asistencias,
                    G_A,
                    G_PK,
                    PK,
                ) = linea  # Desempaquetado de cada linea en sus componentes y almacenarlo en variables
                # Creamos un objeto Jugador pasando las variables declaradas antes como parametros
                jugador = Jugador(
                    int(
                        id.replace(",", "")
                    ),  # Reemplazamos las comas por cadenas vacias
                    jugador,
                    nacionalidad,
                    posicion,
                    club,
                    int(edad.replace(",", "")),
                    int(nacimiento.replace(",", "")),
                    int(partidos_jugados.replace(",", "")),
                    int(partidos_titular.replace(",", "")),
                    int(minutos_jugados.replace(",", "")),
                    float(n.replace(",", "")),
                    int(goles.replace(",", "")),
                    int(asistencias.replace(",", "")),
                    int(G_A.replace(",", "")),
                    int(G_PK.replace(",", "")),
                    int(PK.replace(",", "")),
                )  # Se han remplazado las comas de algunos campos para evitar que la representacion de los millares
                # que podrian ser separados por comas no se interpreten como 1,000 sino como 1000
                Almacen._jugadores.append(jugador)  # Añadimos un jugador a la lista
        return # fromCSV() retorna objetos 'jugadores' y 'cabecera'

    def toCSV(self, ruta: str):
        if ruta != None:
            with open(ruta, "w", newline="") as archivo:
                contenido = csv.writer(archivo)
                contenido.writerow(
                    [
                        "ID",
                        "Jugador",
                        "Nacionalidad",
                        "Posicion",
                        "Club",
                        "Edad",
                        "Born",
                        "MP",
                        "Starts",
                        "Min",
                        "90s",
                        "Goles",
                        "Asistencias",
                        "G+A",
                        "G-PK",
                        "PK",
                    ]
                )  # Escribe la cabecera
                for jugador in self._jugadores:
                    contenido.writerow(
                        [
                            jugador.id,
                            jugador.jugador,
                            jugador.nacionalidad,
                            jugador.posicion,
                            jugador.club,
                            jugador.edad,
                            jugador.nacimiento,
                            jugador.partidos_jugados,
                            jugador.partidos_titular,
                            jugador.minutos_jugados,
                            jugador.n,
                            jugador.goles,
                            jugador.asistencias,
                            jugador.G_A,
                            jugador.G_PK,
                            jugador.PK,
                        ]
                    )
        else:
            print("El archivo", ruta, " no existe")
