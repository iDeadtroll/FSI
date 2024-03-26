import sqlite3
import csv

# Crear conexión

conn = sqlite3.connect("BBDD.sqlite")

# Obtener cursor
cursor = conn.cursor()
header = []


# Ejecutar sentencia para creación de tabla
cursor.execute("CREATE TABLE JUGADORES(ID INTEGER(6), PLAYER VARCHAR(30), NATIONALITY VARCHAR(6), POS VARCHAR(10), CLUB VARCHAR(30), AGE INTEGER(6), BORN INTEGER(6), MP INTEGER(6), STARTS INTEGER(6), MIN INTEGER(8), Ns DECIMAL(3,1), GOALS INTEGER(6), ASSISTS INTEGER(6), G_A INTEGER(6), G_PK INTEGER(6), PK INTEGER(6))")

with open("19_ucl_stats.csv", "r") as archivo:
    contenido = csv.reader(archivo, delimiter=",")
    header = next(contenido)
    # Insertar registro
    for row in contenido:
        cursor.execute("INSERT INTO JUGADORES VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],),)
conn.commit()


# Sentencia "SELECT 1"
cursor.execute("SELECT ID, PLAYER, NATIONALITY, CLUB, AGE FROM JUGADORES WHERE AGE >= 20 And AGE <= 24")
rows = cursor.fetchall()
print("Jugadores con edad entre 20 y 24 años:")
head = ["ID", "PLAYER", "NATIONALITY", "CLUB", "AGE[20,24]"]
print("{:<6} {:<28} {:<12} {:<22} {:<10}\n".format(*head))
for row in rows:
    print("{:<6} {:<28} {:<12} {:<22} {:<10}".format(*row))
    

# Sentencia "SELECT 2"
cursor.execute("SELECT ID, PLAYER, CLUB, MP FROM JUGADORES WHERE CLUB ='Sevilla'")
rows = cursor.fetchall()
print("\nPartidos jugados en el club Sevilla:\n")
head = ["ID", "PLAYER", "CLUB", "MP"]
print("{:<6} {:<28} {:<22} {:<10}\n".format(*head))
for row in rows:
    print("{:<6} {:<28} {:<22} {:<10}".format(*row))


# Sentencia "UPDATE"
cursor.execute("UPDATE JUGADORES SET MP = 10   WHERE  CLUB ='Sevilla' AND MP = '4'")
conn.commit()


# Sentencia "SELECT 3"
cursor.execute("SELECT ID, PLAYER, CLUB, MP FROM JUGADORES WHERE CLUB ='Sevilla'")
rows = cursor.fetchall()
print("\nActualizacion de partidos jugados en el club Sevilla:\n")
head = ["ID", "PLAYER", "CLUB", "MP"]
print("{:<6} {:<28} {:<22} {:<10}\n".format(*head))
for row in rows:
    print("{:<6} {:<28} {:<22} {:<10}".format(*row))
    

# Sentencia "SELECT" compleja
cursor.execute("SELECT CLUB, SUM(GOALS) AS TOTAL_GOLES FROM JUGADORES GROUP BY CLUB ORDER BY TOTAL_GOLES DESC")
rows = cursor.fetchall()
print("\nSuma de goles agrupados por club  y ordenado por total de goles en orden descendente:\n")
print("Club                  | Total Goles\n")
for row in rows:
    print("{:<22}| {:<10}".format(*row))


# Sentencia "DELETE"
cursor.execute("DELETE FROM JUGADORES WHERE CLUB IN (SELECT CLUB FROM JUGADORES GROUP BY CLUB HAVING SUM(GOALS) < 15)")
conn.commit()


# Sentencia "SELECT" compleja
cursor.execute("SELECT CLUB, SUM(GOALS) AS TOTAL_GOLES FROM JUGADORES WHERE CLUB LIKE '%a%' GROUP BY CLUB ORDER BY TOTAL_GOLES ASC")
rows = cursor.fetchall()
print("\nSuma de goles agrupados por club de los clubes que tengan una letra 'a' en su nombre y ordenado"
      "\npor total de goles en orden ascendente:\n")
print("¡Datos actualizados!")
print("Club                  | Total Goles\n")
for row in rows:
    print("{:<22}| {:<10}".format(*row))

# Cerrar conexión
conn.close()
