# Para implementar este ejemplo se especifica la ruta completa al archivo pero la idea es la misma.
print("Ejemplo1")


class ejemplos:
    handle = open(
        "C:\\Users\\joni-\\Documents\\FSI\\EBs\\EjemplosClase\\Tema1\\palabras", "r"
    )
    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    bigcount = None
    bigword = None
    for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
    print(f"La palabra: {bigword}, se repite {bigcount} veces\n")


# Cuando un programa está en ejecución, fluye de un paso al siguiente.
# Como programadores, establecemos “caminos” para que el programa los siga.
# 'Secuencia'
print("Ejemplo2")
x = 2
print(x)
x = x + 2
print(x)

# 'Condicion'
print("\nEjemplo3")
x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finis")

# 'Bucle'
print("\nEjemplo4")
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")

# Expresiones numericas:
print("\nEjemplo5: suma")
xx = 2
xx = xx + 2
print(xx)

print("\nEjemplo6: producto")
yy = 440 * 12
print(yy)

print("Ejemplo7: división")
zz = yy / 1000
print(zz)

print("Ejemplo8: módulo")
jj = 23
kk = jj % 5
print(kk)

print("Ejemplo9: potencia")
print(4**3)

print("Ejemplo10: division entera")
div = 11 // 5
print("11 dividido entre 5: {}".format(div))

# Precedencia de operaciones
# parentesis -> potencia -> producto -> suma -> de izquierda a derecha
print("\nEjemlo11: precedencia de operaciones")
x = 1 + 2**3 / 4 * 5
print(x)

# El tipo importa
print("\nEjemplo12: tipos")
xx = 1
print(type(xx))

temp = 98.6
print(type(temp))

eee = "hello " + "there"
print(type(eee))

# Conversion de tipos:
print("Ejemplo13: Conversion de tipos")
print(float(99) + 100)
i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))

# Division por enteros produce un resultado de punto flotante

print(10 / 2)
print(9 / 2)
print(99 / 100)
print(10.0 / 2.0)
print(99.0 / 100.0)

# Conversion de cadenas

sval = "123"
print(type(sval))
ival = int(sval)
print(type(ival))
print(ival + 1)
nsv = "hello bob"
# niv = int(nsv)

# Entrada de usuario

nam = input("Who are you? ")
print("Welcome", nam)

# Casting entrada de usuario

inp = input("Europe floor?: ")
usf = int(inp) + 1
print("US floor", usf)

# Imprimir con formato
name = "Pepe"
salary = 900
# Usando f-strings (Python 3.6 y superior)
print(f"This is {name} and my salary is {salary:.2f} $/month.")
# Usando str.format()
print("This is {} and my salary is {:.2f} $/month.".format(name, salary))
# Usando printf-style % formatting
print("This is %s and my salary is %.2f $/month." % (name, salary))


# Condicionales

x = 5
if x < 10:

    print("Smaller")

if x > 20:

    print("Bigger")

print("Finis")

# Operadores de comparacion

x = 5
if x == 5:

    print("Equals 5")

if x > 4:

    print("Greater than 4")

if x >= 5:

    print("Greater than or Equals 5")

if x < 6:
    print("Less than 6")
if x <= 5:

    print("Less than or Equals 5")

if x != 6:

    print("Not equal 6")
