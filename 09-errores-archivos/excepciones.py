c = 0
suma = 0

# Para manejar excepciones, errores
# Se usa 'Try:', 'Except', 'Else', y 'Finally'
# De esta manera si el programa falla, no se va a romper y se podra continuar a menos de que el error sea muy
# Grande e impida toda ejecucion o el correcto funcionamiento del codigo.

while c < 3:
    try:
        n = int(input(f'Ingrese un numero {c+1}'))
        suma += n
        c += 1
    
    except:
        print("Error: Ingrese solo numeros enteros")
    
    else:
        print("Todo ha funcionado correctamente")

    finally:
        print("Fin de la ejecucion")

print(f"La suma total es: {suma}")