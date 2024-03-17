diccionario = {
    "265":(265,"Erling Haaland","NOR","FW","Manchester City",22,2000,11,11,841,9.3,12,1,13,11,1),
    "724":(724,"Piotr Zieliński","POL","MF","Napoli",28,1994,10,8,619,6.9,4,2,6,2,2),
    "236":(236,"Olivier Giroud","FRA","FW","Milan",35,1986,12,12,932,10.4,5,2,7,3,2),
    "378":(378,"Robert Lewandowski","POL","FW","Barcelona",33,1988,5,5,441,4.9,5,0,5,5,0),
    "508":(508,"Victor Osimhen","NGA","FW","Napoli",23,1998,6,5,421,4.7,5,0,5,5,0),
    "570":(570,"Rodrygo","BRA","FW","Real Madrid",21,2001,12,10,819,9.1,5,2,7,3,2),
    "611":(611,"Rafa Silva","POR","MF","Benfica",29,1993,10,10,819,9.1,5,2,7,5,0),
    "654":(654,"Mehdi Taremi","IRN","FW","Porto",30,1992,7,7,611,6.8,5,2,7,3,2),
    "409":(409,"João Mário","POR","FW","Benfica",29,1993,10,10,861,9.6,6,2,8,1,5),
    "318":(318,"Vinicius Júnior","BRA","FW","Real Madrid",22,2000,12,11,972,10.8,7,6,13,7,0),
    "423":(423,"Kylian Mbappé","FRA","FW","Paris S-G",23,1998,8,7,651,7.2,7,3,10,6,1),
    "585":(585,"Mohamed Salah","EGY","FW","Liverpool",30,1992,8,7,624,6.9,8,2,10,7,1)
}

def goles_por_partido(dic): # Diccionario por comprension
    return {k: (v[1], round(v[11] / v[7], 2)) if v[7] != 0 else (v[1], 0) for k, v in dic.items()}

goals_by_match = goles_por_partido(diccionario)
# Tomamos el diccionario de la funcion anterior y usamos la funcion map() para
# aplicar la funcion lambda (que muestra dos valores) a la coleccion goals_by_match.
# Todo ello como parte de un un objeto iterable, porque map() devuelve un iterable. 
list(map(lambda item: print(item[0], item[1]), goals_by_match.items()))

