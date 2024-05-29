from db_class import DB
from Producto import Producto
from funciones import *

db = DB("ventas.db")
# Hacermo una vista de 
res = db.select("SELECT * FROM ventas, productos WHERE ventas.producto = producto.id")

ventas=transformar_ventas(res)
print(ventas)
# calcular = calcular_importes(ventas)
print(res)