import sqlite3

def peso_medio():

    conn = sqlite3.connect("equipo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(peso) FROM jugadores WHERE fecha_baja IS NOT null")

    conn.close

    return peso

def jugadores_retirados_delgados():
    peso =peso_medio()

    conn = sqlite3.connect("equipo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT DNI FROM jugadores WHERE peso <" + str(peso)+ "AND fecha_baja IS NOT null")

    fichero = open("jugadores.txt", "wt")

    for fila in cursor:
        fichero.write(fila[0] + "\n")

    fichero.close()
    conn.close()