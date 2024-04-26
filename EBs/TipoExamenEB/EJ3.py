# Escriba una funcion que pregunte al usuario su edad media mediente teclado y la 
# devuelva. La funcion volvera a preguntar la edad si ésta no está comprendida en el 
# intervalo entre '1' y 'n' (donde 'n' es un parametro recibido por la funcion con valor
# por defecto)
# Finalmente devolvera la edad introducida comprendida en dicho intervalo

# Solucion 1: bien

def preguntarEdad(n):
    edad = int(input("Introduzca su edad: "))
    while edad < 1 or edad > n:
        edad = int(input("Introduzca su edad: "))
    return edad

preguntarEdad(18)



# Solucion 2: MEJOR
# Solucion mejor porque se establece 'n' como parametro por defecto
def preguntarEdad(n=18):
    edad = int(input("Introduzca su edad: "))
    while edad < 1 or edad > n:
        edad = int(input("Introduzca su edad: "))
    return edad

preguntarEdad()