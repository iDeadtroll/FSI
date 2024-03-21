from Producto import Producto
def transformar_ventas(lista):
    res=[]
    for tupla in lista:
        d = {"cantidad": tupla[2], "producto": Producto(tupla[8],tupla[9],tupla[10]), "importe":None}
        res.append(d)
    return res

def calcular_importes(ventas):
    lambda dic: {, ... , }
    pass