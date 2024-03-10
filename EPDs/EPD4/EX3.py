f = open("archivo.txt", "r")
d = {}
contenido = f.read()
# Metodo 1
# for i in contenido:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# Metodo 2

for i in contenido:
    d[i] = d.get(i, 0) + 1
print(d)
