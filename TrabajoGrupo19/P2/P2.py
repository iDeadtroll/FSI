class Jugador:
    def __init__(self, ID, jugador, nacionalidad, posicion, club, edad, nacimiento, partido_jugados, partido_titular, minutos_jugados, n, goles, asistencias, G_A, G_PK, PK):
        self.__ID = ID
        self.__jugador = jugador
        self.__nacionalidad = nacionalidad
        self.__posicion = posicion
        self.__club = club
        self.__edad = edad
        self.__nacimiento = nacimiento
        self.__partido_jugados = partido_jugados
        self.__partido_titular = partido_titular
        self.__minutos_jugados = minutos_jugados
        self.__90s = 0
        self.__goles = goles
        self.__asistencias = asistencias
        self.__G_A = G_A
        self.__G_PK = G_PK
        self.__PK = PK

    # Getters
    def get_ID(self):
        return self.__ID

    def get_jugador(self):
        return self.__jugador
    
    def get_Nacionalida(self):
        return self.__nacionalidad

    def get_jugador(self):
        return self.__jugador

    # ... Agrega los métodos getter para los demás atributos

    # Setters
    def set_ID(self, ID):
        self.__ID = ID

    def set_jugador(self, jugador):
        self.__jugador = jugador

    # ... Agrega los métodos setter para los demás atributos


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
        # Implementa la lógica para crear una instancia a partir de un archivo CSV en 'ruta'
        pass

    def toCSV(self, ruta: str):
        # Implementa la lógica para guardar los datos en un archivo CSV en 'ruta'
        pass
