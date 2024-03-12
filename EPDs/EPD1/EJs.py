# Ejercicio 1: Implementar la funcion fibonacci, tomando como primer termino '1'


# Fibonacci recursivo
def fiboRec(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fiboRec(n - 1) + fiboRec(n - 2)


print(fiboRec(3))

# Fibonacci iterativo


def fiboIter(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b


print(fiboIter(4))

# Fibonacci usando diccionario


def fiboDic_1(n):
    dic = {1: 0, 2: 1}

    def fib(n):
        if n in dic:
            return dic[n]
        else:
            dic[n] = fib(n - 1) + fib(n - 2)
            return dic[n]

    return fib(n)


print(fiboDic_1(5))

# # Fibonacci usando diccionario y get()


def fiboDic_2(n):
    dic = {1: 0, 2: 1}

    def fibo(n, dic):
        if n in dic:
            return dic[n]
        else:
            dic[n] = dic.get(n - 1, fibo(n - 1, dic)) + dic.get(n - 2, fibo(n - 2, dic))
            return dic[n]

    return fibo(n, dic)


print(fiboDic_2(6))


# Ejercicio 2: Implementar la funcion esPrimo que indique si el parametro recibido es primo o no.
def esPrimoRecursivo(n, i=2):
    # Caso base: si n es menor que 2, no es primo
    if n < 2:
        return False
    # Caso base: si i es igual a n, entonces hemos llegado al final de la comprobación
    elif i == n:
        return True
    # Si n es divisible por i, entonces no es primo
    elif n % i == 0:
        return False
    # Llamada recursiva a la función es_primo incrementando el valor de i
    else:
        return esPrimoRecursivo(n, i + 1)


print(esPrimoRecursivo(2))


def esPrimoIterativo_1(n):
    # Si n es menor o igual a 1, no es primo
    if n <= 1:
        return False
    # Si n es 2 o 3, es primo
    elif n <= 3:
        return True
    # Si n es divisible por 2 o 3, no es primo
    elif n % 2 == 0 or n % 3 == 0:
        return False
    # Comenzamos a comprobar desde 5 hasta la raíz cuadrada de n
    i = 5
    while i * i <= n:
        # Si n es divisible por i o por i + 2, no es primo
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # Incrementamos i en 6
        i += 6
    # Si n no es divisible por ningún número en el rango, entonces es primo
    return True


def esPrimoIterativo_2(n):  # O(n)
    # Si n es menor o igual a 1, no es primo
    if n <= 1:
        return False
    # Si n es 2 o 3, es primo
    for i in range(2, n):
        if n % i == 0:  # Si n es divisible por i, entonces no es primo
            return False
    return True


print(esPrimoIterativo_2(2))
