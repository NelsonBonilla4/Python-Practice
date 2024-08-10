'''
ENUNCIADO: Ingrese 6 números en una lista y obtenga el número mayor y menor ingresado.

ANÁLISIS: Para la solución de este problema, se requiere que el usuario ingrese 6 números, 
luego el sistema devuelva el número mayor y menor.
'''

# Lista vacía para almacenar los numeros que de el usuario
n = []

# Ciclo para recibir 6 datos del usuario
for x in range(6):
    x = int(input('Ingrese el valor: '))
    n.append(x)

# Se organiza la lista de menor a mayor
n.sort()

# Se imprimen según las posiciones el mayor y el menor
print(f'El numero mayor es: {n[-1]}')
print(f'El numero menor es: {n[0]}')