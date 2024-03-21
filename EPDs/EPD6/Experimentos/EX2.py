def introducir_datos():
    ingresos = []
    gastos = []

    concepto = input("Introduza concepto: ")

    while concepto != "fin":
        importe = float(input("Introduzca un importe: "))
        if importe >= 0:
            ingresos.append((concepto ,importe))
        else:
            gastos.append((concepto, importe))

        concepto = input("Introduzca concepto ('fin para terminar') ")

    return ingresos, gastos

def main():

    ingresos, gastos = introducir_datos()

    total_ingresos = 0
    for ingreso in ingresos:
        print("Concepto", ingreso[0], "Importe: ", ingreso[1])
        total_ingresos += ingreso[1]
    print("Total de ingresos: ",total_ingresos)


    total_gastos = 0
    for concepto, importe in gastos:
        print("Concepto", concepto, "Importe: ", importe)
        total_gastos += importe
    print("Total de ingresos: ",total_gastos)

if __name__ == "__main__":
    main()




