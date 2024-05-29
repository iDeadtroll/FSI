class ejemplos:
    # # Solicita al usuario que introduzca el nombre de un archivo. El nombre del archivo se guarda en la variable 'name'
    name = input("Enter file:")
    # # Abre el archivo cuyo nombre fue introducido por el usuario. El objeto de archivo abierto se guarda en la variable handle
    handle = open(name, "r")
    #  Inicializa un diccionario vacío llamado 'counts'. Este diccionario se utilizará para contar la frecuencia de cada palabra en el archivo.
    counts = dict()
    for line in handle:  # Bucle que recorre cada línea en el archivo.
        #  Divide la línea actual en palabras. La función split() divide una cadena en una lista donde cada palabra es un elemento de la lista.
        words = line.split()
        # # Bucle anidado que recorre cada palabra en la lista de palabras
        for word in words:
            # Incrementa el conteo de la palabra actual en el diccionario counts. Si la palabra no está en el diccionario, la función get() devuelve 0.
            counts[word] = counts.get(word, 0) + 1

    bigcount = None  # Estas variables se utilizarán para rastrear la palabra con la mayor frecuencia.
    bigword = None
    # bucle que recorre cada elemento en el diccionario counts. Cada elemento es una tupla que contiene una palabra y su conteo.
    for word, count in counts.items():
        # Si bigcount es None (lo que significa que es la primera iteración del bucle) o si el conteo actual es mayor que bigcount.
        if bigcount is None or count > bigcount:

            bigword = word  # Si la condición anterior es verdadera, estas líneas actualizan bigword y bigcount con la palabra y el conteo actuales
            bigcount = count
    # Finalmente, esta línea imprime la palabra con la mayor frecuencia y su conteo.
    print(bigword, bigcount)
