# Organizar en modulos como indica la práctica

class Electrodomestico:
    __nombre = ""
    __precio = 0.0

    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def __str__(self):
        return "Nombre: " + self.__nombre + ", Precio " + str(self.__precio)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @precio.setter
    def precio(self, precio):
        self.__precio = precio


class Lavadora(Electrodomestico):
    __carga = 0

    def __init__(self, carga, nombre, precio):
        self.__carga = carga
        super().__init__(nombre, precio)

    def __str__(self):
        return f"{super().__str__()}, Carga: {self.__carga}"

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, nueva_carga):
        self.__carga = nueva_carga


class Televisor(Electrodomestico):
    __pulgadas = 0
    __fullHD = False

    def __init__(self, pulgadas, fullHD, nombre, precio):
        self.__fullHD = fullHD
        self.__pulgadas = pulgadas
        super().__init__(nombre, precio)

    def __str__(self):
        return (
            super().__str__()
            + ", Pulgadas: "
            + str(self.__pulgadas)
            + ", FullHD: "
            + (" Si" if (self.__fullHD) else "No")
        )

    @property
    def pulgadas(self):
        return self.__pulgadas

    @pulgadas.setter
    def pulgadas(self, pulgadas):
        self.__pulgadas = pulgadas

    @property
    def fullHD(self):
        return self.__fullHD

    @fullHD.setter
    def fullHD(self, fullHD):
        self.__fullHD = fullHD


class StockProducto:
    __stock = 0
    __producto = Electrodomestico("", 0.0)

    def __init__(self, stock, producto):
        self.__stock = stock
        self.__producto = producto

    def __str__(self):
        return "Producto: " + str(self.__producto) + ", stock: " + str(self.__stock)

    @property
    def producto(self):
        return self.__producto

    @property
    def stock(self):
        return self.__stock

    @producto.setter
    def producto(self, producto):
        self.__producto = producto

    @stock.setter
    def stock(self, stock):
        self.__stock = stock


class Almacen:

    def __init__(self):
        self.__catalogo = []
        self.__stock = []

    @property
    def catalogo(self):
        return self.__catalogo

    @property
    def stock(self):
        return self.__stock

    def altaCatalogo(self, oElectro):
        self.catalogo.append(oElectro)
        return True

    def entradaStock(self, st):
        self.stock.append(st)
        return "Aniadido"

    def salidaStock(self, nombre, unidades):
        i = 0
        encontrado = False

        while i < len(self.stock) and not encontrado:
            if self.stock[i].producto.nombre == nombre:
                if self.stock[i].stock < unidades:
                    self.stock[i].stock = 0
                else:
                    self.stock[i].stock -= unidades

                encontrado = True

            i += 1

        if encontrado:
            return ""
        else:
            return ""

    def listadoCatalogo(self):
        mensaje = "Catalogo de productos: \n"

        for e in self.catalogo:
            mensaje += e.__str__() + "\n"

        return mensaje

    def listadoStock(self):
        mensaje = "Catalogo de productos: \n"

        for e in self.stock:
            mensaje += e.__str__() + "\n"
        return mensaje

    def numTelevisoresStock(self):
        suma = 0

        for t in self.stock:
            if isinstance(t.producto, Televisor):
                suma = suma + t.stock

        return suma

    def numLavadorasStock(self):
        suma = 0

        for t in self.stock:
            if isinstance(t.producto, Lavadora):
                suma = suma + t.stock

        return suma

    def importeTotalStock(self):
        importeTotal = 0
        for st in self.stock:
            importeTotal += st.stock * st.producto.precio

        return importeTotal


def main():
    # Crear algunos electrodomésticos
    televisor = Televisor(32, True, "Televisor LG", 300.0)
    lavadora = Lavadora(7, "Lavadora Samsung", 500.0)

    # Crear algunos productos de stock
    stock_tv = StockProducto(10, televisor)
    stock_lavadora = StockProducto(5, lavadora)

    # Crear un almacén
    almacen = Almacen()

    # Añadir los electrodomésticos al catálogo
    almacen.altaCatalogo(televisor)
    almacen.altaCatalogo(lavadora)

    # Añadir los productos de stock al almacén
    almacen.entradaStock(stock_tv)
    almacen.entradaStock(stock_lavadora)

    # Imprimir el catálogo y el stock
    print(almacen.listadoCatalogo())
    print(almacen.listadoStock())

    # Probar la salida de stock
    print(almacen.salidaStock("Televisor LG", 2))

    # Imprimir el stock después de la salida
    print(almacen.listadoStock())


if __name__ == "__main__":
    main()
