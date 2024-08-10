'''
area de un circulo = 3.14 * r**2
r = mitad del diametro (1/2 diametro)
'''

# Función para hallar el area y el radio del circulo
def area_circulo(d):
    r = d / 2
    ac = 3.14159 * r**2
    print(f'El radio del circulo es de: {r}\n El area del circulo es de: {ac}')

area_circulo(float(input('Ingrese el valor del diametro: ')))
