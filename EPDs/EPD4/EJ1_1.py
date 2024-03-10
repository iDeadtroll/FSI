import sqlite3


def conectar():
    conn = sqlite3.connect("clientes.db")
    return conn


def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE clientes (
            NIF TEXT PRIMARY KEY,
            nombre TEXT,
            direccion TEXT,
            telefono TEXT,
            correo TEXT,
            vip BOOLEAN
        )
    """
    )
    conn.commit()


def añadir_cliente(conn, NIF, nombre, direccion, telefono, correo, vip):
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)""",
        (NIF, nombre, direccion, telefono, correo, vip),
    )
    conn.commit()


def mostrar_cliente(conn, NIF):
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM clientes WHERE NIF = ?""",
        (NIF,),
    )
    return cursor.fetchone()


def main():
    conn = conectar()
    # crear_tabla(conn)

    while True:
        print(
            "(1) Añadir cliente\n",
            "(2) Mostrar cliente a partir de su NIF\n",
            "(3) Terminar.\n",
        )
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            NIF = input("Introduce el NIF del cliente: ")
            nombre = input("Introduce el nombre del cliente: ")
            direccion = input("Introduce la dirección del cliente: ")
            telefono = input("Introduce el teléfono del cliente: ")
            correo = input("Introduce el correo del cliente: ")
            vip = bool(input("¿Es el cliente VIP? (1 para sí, 0 para no): "))
            añadir_cliente(conn, NIF, nombre, direccion, telefono, correo, vip)
        elif opcion == 2:
            NIF = input("Introduce el NIF del cliente a mostrar: ")
            print(mostrar_cliente(conn, NIF))
        elif opcion == 3:
            break

    conn.close()


if __name__ == "__main__":
    main()
