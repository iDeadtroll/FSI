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


    # @jugador.setter
    # def jugador(self, jugador):
    #     self.__jugador = jugador

    # Para este problema podemos precindir de los metodos modificadores.


    # Método para imprimir las propiedades del objeto Jugador como un string
    def __str__(self):
        campos = ['ID', 'JUGADOR', 'NACIONALIDAD', 'POSICION', 'CLUB', 'EDAD', 'NACIMIENTO', 'PARTIDOS_JUGADOS', 'PARTIDOS_TITULAR', 'MINUTOS_JUGADOS', 'GOLES', 'ASISTENCIAS', 'G+A', 'G+PK', 'PK']
        return '\n'.join(f'{c:<20}: {j}' for c, j in zip(campos, iter(self)))

        

    # Método que toma las propiedades del objeto Jugador para construir un iterable de dicho objeto
    # Usaremos este método para mostrar los campos de cada Jugador con un formato de tabla más adelante
    def __iter__(self):
        yield self.id
        yield self.jugador
        yield self.nacionalidad
        yield self.posicion
        yield self.club
        yield self.edad
        yield self.nacimiento
        yield self.partidos_jugados
        yield self.partidos_titular
        yield self.minutos_jugados
        yield self.n
        yield self.goles
        yield self.asistencias
        yield self.G_A
        yield self.G_PK
        yield self.PK

    # Método de la clase que contiene los tipos de datos de las propiedades en un orden específico
    # Lo usaremos mas edelante para castear los parametros de entrada antes de pasarlos al constructor
    @classmethod
    def tipos(cls):
        return [int, str, str, str, str, int, int, int, int, int, float, int, int, int, int, int]



# Funciones auxiliares para abstraer a las clases que las invocas de buena parte de la logica.
class Funciones: 
    
    
    def validar_datosJugador(self, id: int):
        count = 0
        valido = False
        print("Intoduzca los datos del jugador:")
        while not valido:
            # Pedir los datos del jugador y validar los datos introducidos
            if count > 0:
                print("\nIntoduzca los datos del jugador nuevamente:")
            nombre = input("Nombre: ")
            if not all(palabra.isalpha() for palabra in nombre.split()) or nombre == "":
                print("Error: el nombre debe tener caracteres entre (A/a-Z/z).")
                count+=1
                continue
            
            nacionalidad = input("Nacionalidad: ")
            if not (nacionalidad.isalpha() and len(nacionalidad) == 3):
                print("Error: nacionalidad debe tener 3 caractéres (A-Z).Ejemplo: ESP, ITA, FRA...")
                count+=1
                continue
            
            posiciones_validas = ["FW", "MF", "DF", "GK"]
            pos = input("Posicion: ")
            if pos not in posiciones_validas:
                print("Error: posicion debe ser una de las siguientes: " + ", ".join(posiciones_validas))
                count+=1
                continue
            
            club = input("Nombre del club: ")
            if not all(palabra.isalpha() for palabra in club.split()):
                print("Error: el nombre debe tener caracteres entre (A/a-Z/z).")
                count+=1
                continue

            edad = input("Edad: ")
            if not edad.isdigit() or not 16 <= int(edad) <= 40:
                print("Error: la edad debe ser un número entre 16 y 40.")
                count+=1
                continue
                    
            born = input("Nacimiento: ")
            if not (born.isdigit() and 1980 <= int(born) <= 2024):
                print("Error: el año de nacimiento debe ser un número entre 1980 y 2024.")
                count+=1
                continue
            
            mp = input("Partidos jugados: ")
            if not mp.isdigit():
                print("Error: la entrada debe ser un numero.")
                count+=1
                continue
            
            starts = input("Partidos como titular: ")
            if not starts.isdigit():
                print("Error: la entrada debe ser un numero.")
                count+=1
                continue
            
            min = input("Minutos jugados: ")
            if not min.isdigit():
                print("Error: la entrada debe ser un numero.")
                count+=1
                continue

            n = input("Partidos completos jugados: ")
            if not n.isdigit():
                print("\n\tError: la entrada debe ser un número.")
                count+=1
                continue
            
            goles = input("Goles: ")
            if not goles.isdigit():
                print("Error: la entrada debe ser un numero.")
                count+=1
                continue
            
            asistencias = input("Asistencias: ")
            if not asistencias.isdigit():
                print("Error: la entrada debe ser un numero.")
                count+=1
                continue
            
            g_a = input("Goles más asistencias: ")
            if not g_a.isdigit():
                print("Error: la entrada debe ser un numero.")
                count+=1
                continue
            
            g_pk = input("Goles menos penaltis: ")
            if not g_pk.isdigit():
                print("Error: la entrada debe ser un numero.")
                count+=1
                continue
            
            pk = input("Penaltis: ")
            if not pk.isdigit():
                print("Error: la entrada debe ser un numero.")
                count+=1
                continue
            
            valido = True
        print("Datos del jugador correctos!")
    
        # Crea el objeto Jugador
        jugador = Jugador(id,nombre,nacionalidad, pos,club,int(edad),int(born),int(mp),int(starts),int(min),float(n),int(goles),int(asistencias),int(g_a),int(g_pk),int(pk))
        return  id,jugador
    


    def imprimir_tabla(self,cabecera: list, jugadores: list):
        # Mostramos la cabecera en formato de tabla estableciendo separadores para cada campo
        print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*cabecera))
        # '*jugador' hace referencia a un objeto iterable necesario para recorrer campo a campo del objeto Jugador
        for jugador in jugadores:
            # Mostramos los datos del jugador en formato de tabla estableciendo separadores para cada campo
            print("{:<6} {:<26} {:<12} {:<10} {:<20} {:<10} {:<6} {:<10} {:<6} {:<10} {:<6} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*jugador))

    
    def lista_a_diccionario(self, jugadores: list):        
        edades_por_pais = {} # Diccionario para almacenar las edades de los jugadores por país

        # Recorrer la lista de jugadores
        for jugador in jugadores:
            # Si el país del jugador no está en el diccionario, añadirlo con una lista vacía
            if jugador not in edades_por_pais:
                edades_por_pais[jugador.nacionalidad] = []

            # Añadir la edad del jugador a la lista de su país
            edades_por_pais[jugador.nacionalidad].append(jugador.edad)
        return edades_por_pais
    
    # Eliminar las comas de los datos y convertirlos al tipo correcto
    def limpiar_y_castear(self, dato, tipo): 
        # Si el tipo es igual a 'int' y dato es de la clase 'str'
        if tipo == int and isinstance(dato, str):
            # Limpia y castea 'dato'
            return int(dato.replace(",", ""))
        # Si el tipo es igual a 'float' y dato es de la clase 'str'
        elif tipo == float and isinstance(dato, str):
            return float(dato.replace(",", ""))
        else:
            return dato

    def contenido_a_coleccion(self, contenido: csv.reader, jugadores: list):
        for linea in contenido: # Cada linea es una lista de cadenas que contiene los datos de un jugador
            # Lista por comprensión que genera una nueva lista datos_limpios_casteados.
            # La función zip se utiliza para iterar simultáneamente sobre linea y Jugador.tipos()
            datos_limpios_casteados = [self.limpiar_y_castear(dato, tipo) for dato, tipo in zip(linea, Jugador.tipos())]

            # Con (*datos_limpios_casteados) desempaquetamos los datos de la lista y los pasamos como argumentos al constructor de Jugador
            jugador = Jugador(*datos_limpios_casteados)
            jugadores.append(jugador)
        return jugadores





# Clase que implementa las propiedades y metodos que permiten gestionar la lista de objetos Jugador
class Almacen:

    __funcion = Funciones()

    def __init__(self):
        self.__jugadores = [] # Lista que contendrá los registro de jugadores
        self.__cabecera = [] # Lista que contendrá la cabecera con los nombres de los campos

    @property
    def jugadores(self):
        return self.__jugadores
    
    @property
    def cabecera(self):
        return self.__cabecera
    
    @jugadores.setter
    def jugadores(self, jugadores):
        self.__jugadores = jugadores

    @cabecera.setter
    def cabecera(self, cabecera):
        self.__cabecera = cabecera

    @property
    def funcion(self):
        return self.__funcion
    
        
        
    def altaJugador(self,id: int, jugador: Jugador):
        self.jugadores.append(jugador)
        print(f"Jugador con ID {id} añadido correctamente")

    def bajaJugador(self, id: int):
        for jugador in self.jugadores:
            if jugador.id == id:
                print(jugador)  # Esto invoca a __str__
                self.jugadores.remove(jugador)
                print(f"Jugador con id {id} ha sido eliminado.")
                return
        print(f"No se encontró ningún jugador con id {id}.")

    def listadoJugadores(self):

        self.funcion.imprimir_tabla(self.cabecera ,self.jugadores)


    def agruparPorCampo(self): # Mostrar la media de edad por pais.

        edades_por_pais = self.funcion.lista_a_diccionario(self.jugadores)

        # Diccionario por comprension 'media_edad_por_pais'. Clave 'pais'; Valor 'media de edad'.
        media_edad_por_pais = {pais: sum(edades) / len(edades) for pais, edades in edades_por_pais.items()}
        print(" País", " | Media de Edad")
        print("_________________________")
        for pais, media_edad in media_edad_por_pais.items():
            print(f"{pais}   | {media_edad}")


    def fromCSV(self, ruta: str):

        with open(ruta, "r") as archivo: # Abrimos el archivo en modo lectura
            contenido = csv.reader(archivo, delimiter=",")
           
            self.cabecera = (next(contenido)) # Guardamos la primera linea en la lista 'cabecera'

             # Funcion que hace un tratamiento del contenido para añadirlo a una coleccion.
            self.jugadores = self.funcion.contenido_a_coleccion(contenido,self.jugadores)
            

    def toCSV(self, ruta: str):
        if ruta is not None:
            with open(ruta, "w", newline="") as archivo:
                contenido = csv.writer(archivo)
                contenido.writerow(self.cabecera)  # Escribe la cabecera
                for jugador in self.jugadores: # Escribe el resto de lineas
                    contenido.writerow(list(jugador))  # Convierte el iterador a lista
        else:
            print(f"El archivo {ruta} no existe")
