result_divi = 0

# Podemos atrapar diversos errores con 'Try' y 'Except', cuando el error es desconocido
# podemos usar la linea 17 para averiguar cual es el error, una vez conozcamos el error lo 
# pasamos en el 'except' y con eso ya damos una orden a partir de ese error, ya sea pedirle al 
# usuario que ingrese los datos de manera correcta, a corregir procesos internos de la app
try:
    a = int(input('Ingrese el dividendo: '))
    b = int(input('Ingrese el divisor: '))

    result_divi = a / b

except ValueError:
    print('Error: Ingrese solo numeros enteros!')

except ZeroDivisionError:
    print('Error: No se puede dividir entre cero')

except Exception as error:
    print('Ha ocurrido un error no previsto', type(error).__name__)

print(f'El resultado es de: {result_divi}')
    