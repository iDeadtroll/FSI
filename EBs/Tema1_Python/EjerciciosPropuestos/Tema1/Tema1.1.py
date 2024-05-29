# EJERCICIO 1 (Transaparencia 42)
# Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = int(input("Introduzca el numero de horas trabajadas: "))
salario_hora = int(input("Introduzca el salario por hora: "))

paga = horas_trabajadas * salario_hora

print("La paga correspondiente es: " + str(paga))


# EJERCICIO 2
# Resecribe el programa anterior para que el coste por hora sea 1.5 veces superior cuando las horas de
# trabajo esten por encima de las 40.

horas_trabajadas = int(input("Introduzca el numero de horas trajadas: "))
salario_hora = int(input("Introduzca el salario por hora: "))

paga = 0

if horas_trabajadas > 40:

    paga = (horas_trabajadas - 40) * (salario_hora * 1.5) + salario_hora * 40

else:

    paga = horas_trabajadas * salario_hora

print("La paga correspondiente es: " + str(paga))
