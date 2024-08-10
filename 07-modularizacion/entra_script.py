import sys

# Básicamente al ejecutar el archivo tomará como argumentos los que vaya después del llamado
# Ej: python entra_script.py
# ['entra_script.py', '5']
text = sys.argv
print(text)

nombre = 'Nelson'
edad = 17
altura = 165
# Una forma distinta de hacer el format. print(f'Nombre: {nombre}')
print('Nombre: {} \nEdad: {} \nAltura: {}cm'.format(nombre,edad,altura))
# Asigna a cada llave una variable según el orden en que se le pase

# Sub variante de la anterior que sirve para especificar posiciones
print('Nombre: {a} \nEdad: {b} \nAltura: {c}cm'.format(a=nombre,b=edad,c=altura))