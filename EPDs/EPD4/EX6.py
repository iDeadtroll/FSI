import sqlite3

# Crear conexión
conn = sqlite3.connect("mydatabase.db")
# Obtener cursor
cursor = conn.cursor()
# Ejecutar sentencia de creación de tabla
cursor.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text,salary real)")
conn.commit()
# Ejecutar sentencia de inserción
cursor.execute("INSERT INTO employees VALUES(1, 'John', 700)")
cursor.execute("INSERT INTO employees VALUES(2, 'Ana', 800)")
cursor.execute("INSERT INTO employees VALUES(3, 'Toni', 100)")
conn.commit()
# Recorriendo las filas devueltas por fetchall
cursor.execute("SELECT id, name FROM employees")
cursor.execute("SELECT SUM(salary) FROM employees")

rows = cursor.fetchall()
for row in rows:
    print(row)
# Recorriendo fila a fila con fetchone
cursor.execute("SELECT id, name FROM employees")
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()
# Usando el cursor como un iterador
cursor.execute("SELECT id, name FROM employees")
for row in cursor:
    print(row)
cursor.execute('update employees set name="JUAN" where id=1')
conn.commit()
conn.close()
