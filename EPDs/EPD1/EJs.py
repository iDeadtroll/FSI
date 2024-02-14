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
