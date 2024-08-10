'''
Sistema para reconocer si un numero es par o impar
0 es neutro
'''

# funcion para detectar si es par o impar y si es negativo o positivo
def pppn0(n):
    if n % 2 == 0 and n > 0:
        print(f'El numero {n} es par positivo')

    elif n % 2 == 0 and n < 0:
        print(f'El numero {n} es par negativa')

    elif n % 2 != 0 and n > 0:
        print(f'El numero {n} es impar positivo')
    
    elif n == 0:
        print(f"El numero {n} es neutro")
    else:
        print(f'El numero {n} es impar negativo')

pppn0(float(input('Ingrese su numero: ')))