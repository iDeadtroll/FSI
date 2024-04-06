class DatosEntrada:
    # t_busqueda se da en 'milisegundos' y hay que convertirlo ha 'segundos'
    # v_rotacional se da en 'rpm' y hay que pasarlo ha 'rps o pistas/segundo'
    def __init__(self, t_busqueda: int, v_rotacional: int, sectores_pista: int, bytes_sector: int):
        self.__t_busqueda = t_busqueda
        self.__v_rotacional = v_rotacional
        self.__sectores_pista = sectores_pista
        self.__bytes_sector = bytes_sector

    @property
    def t_busqueda(self):
        return self.__t_busqueda / 1000

    @property
    def v_rotacional(self):
        return self.__v_rotacional / 60

    @property
    def sectores_pista(self):
        return self.__sectores_pista

    @property
    def bytes_sector(self):
        return self.__bytes_sector
    
    @t_busqueda.setter
    def t_busqueda(self, t_busqueda):
        self.__t_busqueda = t_busqueda

    @v_rotacional.setter
    def v_rotacional(self, v_rotacional):
        self.__v_rotacional = v_rotacional

    @sectores_pista.setter
    def sectores_pista(self, sectores_pista):
        self.__sectores_pista = sectores_pista

    @bytes_sector.setter
    def bytes_sector(self, bytes_sector):
        self.__bytes_sector = bytes_sector

    def __str__(self):
        datos = ""
        datos += "Datos de entrada: \n"
        datos += "Tiempo de busqueda = " + str(self.t_busqueda) + " segundos\n"
        datos += "Velocidad rotacional = " + str(self.v_rotacional) + " pistas/segundo\n"
        datos += "Sectores por pista = " + str(self.sectores_pista) + " sectores/pista\n"
        datos += "Bytes por sector = " + str(self.bytes_sector) + " bytes/sector"
        return datos

