'''
Crear un modulo que genere una secuencia de Fibonacci, dentro de este módulo crea dos funciones:

La primera función que genere la secuencia de Fibonacci con números

La segunda función que retorne una lista de secuencia de Fibonacci


Fibonacci == es una secuencia en la que cada número es la suma de los dos anteriores.
'''
'''
def fibonacci(y):
    count = 0
    x = 0
    n = 1
    z = 0
    fibo = []
    while count < y:
        print(f'x = {x}')
        fibo.append(x)
        z = n + x
        x = n
        n = z
        count += 1
        fibo.append(n)
        print(f'El anterior es {x}, el actual {n}')
    return fibo
    # print(f'Los numeros finales son: {x,n}')
    

    

def fibonacci_sec():
    fibo = fibonacci(9)
    print(' '*4)
    print('***' * 4)
    print('SECUENCIA FIBONACCI:', '\n', ' '*4)
    print(fibo)
    print('NOTA: Se lee que el de adelante es el anterior, exceptuando el cero. Como por ejemplo con el 2, sería que 2 y su anterior 1 es igual a 3. Así sucesivamente.')

if __name__ == "__main__":
    fibonacci_sec()

'''

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result