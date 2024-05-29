# Escriba una clase que contenga tres propiedades: salario bruto, salario neto e IRPF. Suponga que el salario
# neto es la diferencia entre el salario bruto y el IRPF(suponga tambien que el valor del IRFP introducido por 
# el usuario es positivo). Programe un constructor para la clase que reciba el salario bruto y el IRPF(el 
# salario neto se calcula en dicho constructor). Programe un método modificador para la propiedad del salario 
# bruto de manera que no se permita almacenar dicho salario negativo o si el valor es inferior al de la
# propiedad IRPF. En tal caso, escribir un mensaje al usuario indicando tal error. Además, dicho modificador
# deberá actualizar el valor de la propiedad del salario neto convenientemente. No se pide ningun otro metodo.

class Empleo:

    def __init__(self, salarioBruto : float, IRPF: float):
        self.__salarioBruto = salarioBruto
        self.__irpf = IRPF
        self.__salarioNeto = salarioBruto - IRPF


    def salarioBruto(self, sBruto):
        if sBruto < 0 or sBruto < self.__irpf:
            print("Error: el salario bruto no debe ser menor que 0 ó menor IRPF")

        else:
            self.__salarioBruto = sBruto
            self.__salarioNeto = self.__salarioBruto - self.__irpf


