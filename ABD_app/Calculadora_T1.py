
from DatosEntrada import DatosEntrada


class Calculadora_T1(DatosEntrada):

    def t_latencia_rot(self):
        return 1/self.v_rotacional
    
    def t_medio_latencia_rot(self):
        return 1/(2*self.v_rotacional)

    def t_acceso(self):
        return self.t_busqueda + self.t_medio_latencia_rot()
    
    def __str__(self):
        datos = super().__str__()
        datos += "\n\nCalculo 1: "
        datos += "\nTiempo de acceso: " + str(round(self.t_acceso(),4))
        return datos

    
tiempo1 = Calculadora_T1(6,4500,20,512)
print(tiempo1)
