class Transaccion:
    __inmuebles = ("CASA","PISO","GARAGE")

    def __init__(self, direccion: str, poblacion:str, cod_postal:int, provincia:str, tipo_inmueble:int, comision:int):
        self.__direccion = direccion
        self.__poblacion = poblacion
        self.__cod_postal = cod_postal
        self.__provincia = provincia
        self.__tipo_inmueble = tipo_inmueble
        self.__comision = comision
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion
    
    @poblacion.setter
    def poblacion(self, poblacion):
        self.__poblacion = poblacion
    
    @cod_postal.setter
    def cod_postal(self, cod_postal):
        self.__cod_postal = cod_postal
    
    @provincia.setter
    def provincia(self, provincia):
        self.__provincia = provincia
    
    @tipo_inmueble.setter
    def tipo_inmueble(self, tipo_inmueble):
        self.__tipo_inmueble = tipo_inmueble
    
    @comision.setter
    def comision(self, comision):
        self.__comision = comision

    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def poblacion(self):
        return self.__poblacion
    
    @property
    def cod_postal(self):
        return self.__cod_postal
    
    @property
    def provincia(self):
        return self.__provincia
    
    @property
    def tipo_inmueble(self):
        return self.__tipo_inmueble
    
    @property
    def comision(self):
        return self.__comision
    
    def __str__(self):
        datos: str = ""
        datos += "Direccion: " + self.__direccion + "\n"
        datos += "Poblacion: " + self.__poblacion + "\n"
        datos += "CP: " + self.__cod_postal + "\n"
        datos += "Provincia: " + self.__provincia + "\n"
        datos += "Tipo inmueble: " + self.__tipo_inmueble + "\n"
        datos += "Comision: " + self.__comision + "\n"

        return datos