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

    __jugadores = list() # Lista que contendrá los registro de jugadores
    __cabecera = list()  # Lista que contendrá la cabecera con los nombres de los campos

    def __init__(self):
        self.__jugadores = []
        self.__cabecera = []

    # @property
    def jugadores(self):
        return self.__jugadores
    
    # @property
    def cabecera(self):
        return self.__cabecera
    
        
        
    def altaJugador(self):
        msg = 0
        valido = False
        print("Intoduzca los datos del jugador:")
        while not valido:
            # Pedir los datos del jugador validar los datos
            if msg > 0:
                print("Intoduzca los datos del jugador nuevamente:")
            nombre = input("Nombre: ")
            if not all(palabra.isalpha() for palabra in nombre.split()) or nombre == "":
                print("Error: el nombre debe tener caracteres entre (A/a-Z/z).")
                msg+=1
                continue
            
            nacionalidad = input("Nacionalidad: ")
            if not (nacionalidad.isalpha() and len(nacionalidad) == 3):
                print("Error: nacionalidad debe tener 3 caractéres (A-Z).Ejemplo: ESP, ITA, FRA...")
                msg+=1
                continue
            
            posiciones_validas = ["FW", "MF", "DF", "GK"]
            pos = input("Posicion: ")
            if pos not in posiciones_validas:
                print("Error: posicion debe ser una de las siguientes: " + ", ".join(posiciones_validas))
                msg+=1
                continue
            
            club = input("Nombre del club: ")
            if not all(palabra.isalpha() for palabra in club.split()):
                print("Error: el nombre debe tener caracteres entre (A/a-Z/z).")
                msg+=1
                continue

            edad = input("Edad: ")
            if not edad.isdigit() or not 16 <= int(edad) <= 40:
                print("Error: la edad debe ser un número entre 16 y 40.")
                msg+=1
                continue
                    
            born = input("Nacimiento: ")
            if not (born.isdigit() and 1980 <= int(born) <= 2024):
                print("Error: el año de nacimiento debe ser un número entre 1980 y 2024.")
                msg+=1
                continue
            
            mp = input("Partidos jugados: ")
            if not mp.isdigit():
                print("Error: la entrada debe ser un numero.")
                msg+=1
                continue
            
            starts = input("Partidos como titular: ")
            if not starts.isdigit():
                print("Error: la entrada debe ser un numero.")
                msg+=1
                continue
            
            min = input("Minutos jugados: ")
            if not min.isdigit():
                print("Error: la entrada debe ser un numero.")
                msg+=1
                continue

            n = input("Partidos completos jugados: ")
            try:
                n_float = float(n)
                if n_float < 0:
                    print("Error: la entrada debe ser un número positivo.")
                    msg+=1
                    continue
            except ValueError:
                print("Error: la entrada debe ser un número decimal.")
                msg+=1
                continue
            
            goles = input("Goles: ")
            if not goles.isdigit():
                print("Error: la entrada debe ser un numero.")
                msg+=1
                continue
            
            asistencias = input("Asistencias: ")
            if not asistencias.isdigit():
                print("Error: la entrada debe ser un numero.")
                msg+=1
                continue
            
            g_a = input("Goles más asistencias: ")
            if not g_a.isdigit():
                print("Error: la entrada debe ser un numero.")
                msg+=1
                continue
            
            g_pk = input("Goles menos penaltis: ")
            if not g_pk.isdigit():
                print("Error: la entrada debe ser un numero.")
                msg+=1
                continue
            
            pk = input("Penaltis: ")
            if not pk.isdigit():
                print("Error: la entrada debe ser un numero.")
                msg+=1
                continue
            
            valido = True
        print("Datos del jugador correctos!")
        id  = len(self.__jugadores) + 1
    
        # Crea el objeto Jugador
        j = Jugador(id,nombre,nacionalidad, pos,club,int(edad),int(born),int(mp),int(starts),int(min),float(n),int(goles),int(asistencias),int(g_a),int(g_pk),int(pk))

        self.__jugadores.append(j)
        print(f"Jugador con ID {id} añadido correctamente")

    def bajaJugador(self, id: int):
        for jugador in self.__jugadores:
            if jugador.id == id:
                self.__jugadores.remove(jugador)
                print(f"Jugador con id {id} ha sido eliminado.")
                return
        print(f"No se encontró ningún jugador con id {id}.")


    def listadoJugadores(self):

        # Mostramos la cabecera en formato de tabla estableciendo separadores para cada campo
        for cabecera in self.__cabecera:
            print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*cabecera))
        # '*jugador' hace referencia a un objeto iterable necesario recorrer campo a campo del objeto Jugador
        for jugador in self.__jugadores:
            # Mostramos los datos del jugador en formato de tabla estableciendo separadores para cada campo
            print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*jugador))



    def agruparPorCampo(self): # Motrar la media de edad por pais.
        # Diccionario para almacenar las edades de los jugadores por país
        edades_por_pais = {}

        # Recorrer la lista de jugadores
        for jugador in self.__jugadores:
            # Si el país del jugador no está en el diccionario, añadirlo con una lista vacía
            if jugador not in edades_por_pais:
                edades_por_pais[jugador.nacionalidad] = []

            # Añadir la edad del jugador a la lista de su país
            edades_por_pais[jugador.nacionalidad].append(jugador.edad)

        # Calcular la media de edad para cada país
        media_edad_por_pais = {pais: sum(edades) / len(edades) for pais, edades in edades_por_pais.items()}
        print(" País", " | Media de Edad")
        print("_________________________")
        for pais, media_edad in media_edad_por_pais.items():
            print(f"{pais}   | {media_edad}")


    def fromCSV(self, ruta: str):

        with open(ruta, "r") as archivo:
            contenido = csv.reader(
                archivo
            )   # Creamos un objeto contenido para despues iterar linea a linea
                # Añadimos la primera linea desde contenido a la lista cabecera
            self.__cabecera.append(next(contenido))
            for linea in contenido:  # Recorremos contenido linea a linea y desempaquetamos
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
                ) = linea  # Desempaquetado de cada linea en sus componentes para almacenarlo en variables
                    # Creamos un objeto Jugador pasando las variables antes declaradas como parametros
                jugador = Jugador(
                    int(
                        id.replace(",", "") # Reemplazamos las comas por cadenas vacias
                    ),  
                    jugador,
                    nacionalidad,
                    posicion,
                    club,
                    int(edad.replace(",", "")), # Casting del campo a entero
                    int(nacimiento.replace(",", "")),
                    int(partidos_jugados.replace(",", "")),
                    int(partidos_titular.replace(",", "")),
                    int(minutos_jugados.replace(",", "")),
                    float(n.replace(",", "")), # Casting del campo a float
                    int(goles.replace(",", "")),
                    int(asistencias.replace(",", "")),
                    int(G_A.replace(",", "")),
                    int(G_PK.replace(",", "")),
                    int(PK.replace(",", "")),
                )   # Se han remplazado las comas de algunos campos para evitar que la representacion de los millares
                    # que podrian estar separados por comas para que no se interpreten como 1,000 sino como 1000
                self.__jugadores.append(jugador)  # Añadimos un jugador a la lista

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
                for jugador in self.__jugadores:
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
