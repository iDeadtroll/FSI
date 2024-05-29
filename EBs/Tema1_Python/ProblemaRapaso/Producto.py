class Producto:
    def __init__(self, nombre, precio_unitario, coste):
        self.__nombre = nombre
        self.__precio_unitario = precio_unitario
        self.__coste = coste
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio_unitario(self):
        return self.__precio_unitario
    
    @nombre.setter
    def precio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario

    @property
    def coste(self):
        return self.__coste
    
    @nombre.setter
    def coste(self, coste):
        self.__coste = coste
    
