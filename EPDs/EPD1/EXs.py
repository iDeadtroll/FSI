# Experimento 1
a = 15
b = 4
print ("""La división entera:""" + a + " entre " + b + " es " + a // b + " resto " + a % b)
print ("""La división
real:""", a, "entre", b, "es", a / b)

# Experimento 1 Resuelto
a = 15
b = 4
print ("""La división entera:""" , a , " entre " , b , " es " , a // b , " resto " , a % b)
print ("""La división real:""", a, "entre", b, "es", a / b)

# Experimento 2
cuentas = [(300,450),(400,300),(500,350),(450,300)]
# el primer numero indica ingresos, el segundo gastos.
impares = cuentas[::2]
pares = cuentas[???]
dosPrimeros = cuentas[:2]
dosUltimos = cuentas[???]
primeroYultimo = ???

# Experiemtno 2 Resuelto
cuentas = [(300,450),(400,300),(500,350),(450,300)]
print(cuentas)
print("Tamanyo de la lista ", len(cuentas))
# el primer numero indica ingresos, el segundo gastos.
impares = cuentas[::2]
print(impares)
pares = cuentas[1::2]
print(pares)    
dosPrimeros = cuentas[:2]
print(dosPrimeros)
dosUltimos = cuentas[-2:]
print(dosUltimos)
primeroYultimo = [cuentas[0],cuentas[-1]]
print(primeroYultimo)

# Experimento 3: 
cuentas = {"sevilla" : [300,450],
           "madrid" : [400,300], 
           "segovia" : [500,350], 
           "valencia" : [450,300]} 
# el primer numero indica ingresos, el segundo gastos.
cuentasMadridYSegovia = ???
cuentas["sevilla"] = cuentas["sevilla"] + [True]
sumaIngresos = ???

# Experimento 3 Resuelto: 
cuentas = {"sevilla" : [300,450],
           "madrid" : [400,300], 
           "segovia" : [500,350], 
           "valencia" : [450,300]} 
# el primer numero indica ingresos, el segundo gastos.
cuentasMadridYSegovia = [cuentas['madrid'], cuentas['segovia']]
print(cuentasMadridYSegovia)
cuentas["sevilla"] = cuentas["sevilla"] + [True]
print(cuentas['sevilla'])
sumaIngresos = cuentas['sevilla'][0] + cuentas['madrid'][0] + cuentas['segovia'][0] + cuentas['valencia'][0]
print(sumaIngresos)
print(cuentas["sevilla"])

# Experimento 4
cuentas = {("sevilla",41013) : [300,450,True], 
           ("madrid",18650) : [400,300,False],
           ("segovia",28901) : [500,350,False], 
           ("segovia",28902) : [450,500,True]}
# el primer elemento indica ingresos, el segundo gastos y tercero si la diferencia es negativa.
if ???:
print ("Alguna de las cuentas de Segovia es negativa")
else:
print ("Todas las cuentas de Segovia son positivas")
mensaje = "Sevilla (41013) " + ("no " if (cuentas[("sevilla",41013)][2]) else "") + "tiene su
cuenta positiva"
print (mensaje)

# Experimento 4 Resuelto
cuentas = {("sevilla",41013) : [300,450,True], 
           ("madrid",18650) : [400,300,False], 
           ("segovia",28901) : [500,350,False], 
           ("segovia",28902) : [450,500,True]}
# el primer elemento indica ingresos, el segundo gastos y tercero si la diferencia es negativa.
if (cuentas[("segovia",28901)][2] or cuentas[("segovia",28902)][2]):
    print ("Alguna de las cuentas de Segovia es negativa")
else:
    print ("Todas las cuentas de Segovia son positivas")
mensaje = "Sevilla (41013) " + ("no " if (cuentas[("sevilla",41013)][2]) else "") + "tiene su cuenta positiva"
print (mensaje)

# Experimento 5
cuentas = {("sevilla",41013) : [300,450,True], 
           ("madrid",18650) : [400,300,False],
           ("segovia",28901) : [500,350,False], 
           ("segovia",28902) : [450,500,True]}
balancesPositivos = []
for x in cuentas.values():
print(x)
if ???:
balancesPositivos.???
print ("Balances positivos:", balancesPositivos)
umbral = int(input("Indique umbral minimo de balance positivo para buscar:"))
encontrado = False
i = 0
while ???:
if balancesPositivos[i] >=umbral:
encontrado = True
else:
i += 1
if encontrado:
print ("Se ha encontrado este balance: " + str(balancesPositivos[i]))
else:
print ("No se ha encontrado ningun balance superior al umbral.")

# Experimento 5 Resuelto
cuentas = {("sevilla",41013) : [300,450,True], 
           ("madrid",18650) : [400,300,False],
           ("segovia",28901) : [500,350,False], 
           ("segovia",28902) : [450,500,True]}
balancesPositivos = []
for x in cuentas.values():
    print(x)
    if not x[2]:
        balancesPositivos.append(x[0]-x[1])
print ("Balances positivos:", balancesPositivos)
umbral = int(input("Indique umbral minimo de balance positivo para buscar:"))
encontrado = False
i = 0
while not encontrado and i < len(balancesPositivos):
    if balancesPositivos[i] >=umbral:
        encontrado = True
    else:
        i += 1
if encontrado:
        print ("Se ha encontrado este balance: " + str(balancesPositivos[i]))
else:
        print ("No se ha encontrado ningun balance superior al umbral.")