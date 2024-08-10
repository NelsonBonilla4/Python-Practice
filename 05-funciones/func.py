# '*args' permite que se le pueda pasar cualquier cantidad y tipo de datos a la funcion. Tupla
# '**kwargs' permite pasarle a la funcion variables que se definen en el mismo llamado. Diccionario
def sumar(*args, **kwargs):
    print(args)

sumar(1,2,3,'4',4.4, nombre = 'Juja')
