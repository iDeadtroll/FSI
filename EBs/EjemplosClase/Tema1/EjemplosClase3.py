# POO

class PartyAnimal:
    x = 0

    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

# Construc y desctruc
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42 # Se destruye la instancia del objeto 'an' y se sustituye por '42'
print('an contains',an)


class PartyAnimal:

    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name,"constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()

# HERENCIA

class PartyAnimal: # Clase padre

    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name,"constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal): # Clase hija

    points = 0
    def touchdown(self):

        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)
        
        
# ENCAPSULAMIENTO

# Publico

class Venta:
    importe = 0
    def __init__(self, x):
        self.importe = x

v = Venta(1000)
print(v.importe)

# Privado

class Venta:
    importe = 0
    def __init__(self, x):
        self.__importe = x

v = Venta(1000)
print(v.__importe)

# Privado con metodos getters y setters
class Venta:
    __importe = 0
    def __init__(self, x):
        self.__importe = x

    @property
    def importe(self):
        return self.__importe

    @importe.setter
    def importe(self, importe):
        self.__importe = importe
        
        v = Venta(1000)

print( v.getImporte() ) # JAVA

print( v.importe ) # Python

v.setImporte(100); # JAVA

v.importe = 100 # Python

# Métodos Mágicos