class ejemplos:
    def ejemplo1():  # Buscar un numero en una lista
        s = [9, 10, 11, 49, 46]
        x = int(input("Enter a number: "))
        i = 0
        found = False
        while not found and i < len(s):
            if s[i] == x:
                found = True
            i += 1
        if found:
            print("Found!")
        else:
            print("Not found!")

    print("Busqueda usando un bucle 'while'")
    ejemplo1()

    def ejemplo2():
        s = [9, 10, 11, 49, 46]
        x = int(input("Enter a number: "))
        found = x in s
        print("Found!" if found else "Not found!")

    print("Busqueda usando funcion de busqueda 'in'")
    ejemplo2()
