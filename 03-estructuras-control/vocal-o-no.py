'''
Crear una lista con las vocales. 
Si el caracter ingresado no esta en la lista,
No es una vocal
'''

vocales = ['A', 'E', 'I', 'O', 'U']

def verifica_vocal(caracter):
    c = caracter.upper()
    if c in vocales:
        print(f'El caracter {caracter} es una vocal')

    else:
        print(f'El caracter {caracter} no es una vocal')

verifica_vocal(input('Ingrese el caracter a verificar: '))
