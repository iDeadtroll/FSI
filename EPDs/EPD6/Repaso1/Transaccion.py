
class Transaccion:
    __inmuebles = ("CASA", "PISO", "GARAGE")
    __comision: int
    def __init__(self, direccion: str, poblacion: str, cod_postal: int, provincia: str, tipo_inmueble: int):
        self.__direccion = direccion
        self.__poblacion = poblacion
        self.__cod_postal = cod_postal
        self.__provincia = provincia
        self.__tipo_inmueble = tipo_inmueble


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

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @poblacion.setter
    def poblacion(self, poblacion):
        self.__poblacion = poblacion

    @cod_postal.setter
    def cod_postal(self, cod_postal):
        if cod_postal < 0 or cod_postal > 99999:
            print("Error: codigo postal incorrecto. Valor por defecto igual a 0")
            self.__cod_postal = 0
        else:
            self.__cod_postal = cod_postal
    @provincia.setter
    def provincia(self, provincia):
        self.__provincia = provincia
    @tipo_inmueble.setter
    def tipo_inmueble(self, tipo_inmueble):
        self.__tipo_inmueble = tipo_inmueble
    @comision.setter
    def comision(self, comision):
        if comision < 0 or comision > 100:
            print("Error: valor de comision incorrecta. Valor por defecto igual a 5%")
            self.__comision = 5
        else:
            self.__comision = comision



    def __str__(self):
        datos: str = ""
        datos += "Direccion: " + self.__direccion + "\n"
        datos += "Poblacion: " + self.__poblacion + "\n"
        datos += "CP: " + str(self.__cod_postal) + "\n"
        datos += "Provincia: " + self.__provincia + "\n"
        datos += "Tipo inmueble: " + self.__inmuebles[self.__tipo_inmueble-1] + "\n"
        # datos += "Comision: " + str(self.__comision) + " %" + "\n"

        return datos



class Alquiler(Transaccion):

    __arrendador: str
    __arrendatario: str
    __amueblado: bool
    
    def __init__(self, direccion: str, poblacion: str, cod_postal: int, provincia: str, tipo_inmueble: int):
        super().__init__(direccion, poblacion, cod_postal, provincia, tipo_inmueble)
