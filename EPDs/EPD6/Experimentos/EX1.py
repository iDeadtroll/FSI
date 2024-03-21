import math

a = float(input("Introduzca el coefircionete a"))
b = float(input("Introduzca el coefircionete b"))
c = float(input("Introduzca el coefircionete c"))

discriminante = b*b -4*a*c
if discriminante < 0:
    print("No hay resultado real")
elif discriminante == 0:
    resultado = -b/(2*a)
    print("Resultado es unico:", resultado)
else:
    r1 = (-b + math.sqrt(discriminante))/(2*a)
    r2 = r1 = (-b - math.sqrt(discriminante))/(2*a)
    print("El primer resultado es", r1)