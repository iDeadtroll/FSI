f = open("archivo.txt", "r")

contenido = f.read()

c = len(contenido)
print(c)
f.close()
