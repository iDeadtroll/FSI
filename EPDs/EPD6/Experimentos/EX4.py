dias_validos=['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

nombre = input("Introduzca nombre: ")

dia = input("Introduzca el dia: ")

dic = {}
while len(dic) < len(dias_validos):
    if dia in dias_validos:
        i = 0
        if nombre not in dic.get():
            dic[nombre] = dia[i]
            i+=1
        
    else: 
        print("Dia no valido")

