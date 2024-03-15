import csv


class Jugador:

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

    def __str__(self):
        return f"{self.__id} {self.__jugador} {self.__nacionalidad} {self.__posicion} {self.__club} {self.__edad} {self.__nacimiento} {self.__partidos_jugados} {self.__partidos_titular} {self.__minutos_jugados} {self.__goles} {self.__asistencias} {self.__G_A} {self.__G_PK} {self.__PK}"

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


class Almacen:

    def __init__(self):
        self._jugadores = []

    def altaJugador(self, j: Jugador):
        self._jugadores.append(j)
        return j

    def bajaJugador(self, ID: int):
        pass

    def listadoJugadores(self):
        return self._jugadores

    def agruparPorCampo(self, campo: str):
        return {getattr(j, campo): j for j in self._jugadores}

    @staticmethod
    def fromCSV(ruta: str):
        jugadores = []

        with open(ruta, "r") as archivo:
            lector = csv.reader(archivo)
            cabecera = next(lector)  # Saltamos la cabecera
            for fila in lector:
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
                ) = fila
                jugador = Jugador(
                    int(id.replace(",", "")),
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
                )
                jugadores.append(jugador)
        return jugadores, cabecera

    def toCSV(self, ruta: str):
        # Implementa la lógica para guardar los datos en un archivo CSV en 'ruta'
        pass
