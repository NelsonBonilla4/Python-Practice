'''
Lo que vemos abajo es una forma de crear un archivo y editarlo, 'w' viene siendo la forma en la
que abrimos el archivo, aunque hay que tener cuidado ya que con 'w' borramos y escribimos desde cero todo 
el archivo, haciendo que se pierda informacion. Esta escritura hay que hacerla antes del 'close()'
'''
from io import open
from os import path

def escribir_archivo():
    archivo = open('UwU.txt', 'w')
    archivo.write('Hola broer, todo bem?')
    archivo.close()

#escribir_archivo()

'''
Lo siguiente es el como leemos un archivo una vez creado, primero importamos 'path' de 'os' para asi 
checar que efectivamente exista el archivo y evitar un error.
Abrimos de la misma manera de ahorita, salvo que ahora usamos 'r' (read), en vez de 'w' (write)
Tenemos varias formas de leer, como las siguientes:

archivo.read()  (Nos imprime todo como un print)
archivo.readline()   (Nos imprimer una linea)
archivo.readlines()   (Nos imprime todo como una lista)

'''

def leer_archivo():
    if path.isfile('./UwU.txt'):
        archivo = open('UwU.txt', 'r')
        # texto = archivo.read()
        texto = archivo.readlines()
        archivo.close()

        print(texto)
    else:
        print('No se encontro el archivo')

leer_archivo()

'''
De la siguiente manera agregamos datos a un archivo. primero lo abrimos con la instruccion 'a' (add), para
asi actualizar los datos y añadir a partir de la ultima linea en la que se estaba.
'''

def agregar_datos():
    if path.isfile('./UwU.txt'):
        archivo = open('UwU.txt', 'a')
        archivo.write('\nNeruson-samaaaaaaa!!!!!!!')
        archivo.close()
    
    else:
        print('No se encontro el archivo')
    
#agregar_datos()

'''
Con lo siguiente modificamos ya lo que tenga el archivo, como vimos antes la forma 'readlines()' devuelve
la informacion del archivo como una lista, y esa lista la podemos editar y mas adelante pasarla a 'writelines()'
para de esta manera editar la informacion de nuestro archivo.

para poder leer y editar al mismo tiempo ponemos 'r+' (read, write)

archivo.seek() (Nos permite ubicar el cursor en la parte que queramos, ya sea en el caracter 1, o en el 16)
'''

def modificar_datos():
    if path.isfile('./UwU.txt'):
        archivo = open('UwU.txt', 'r+')
        texto = archivo.readlines()
        print(texto)
        texto[1] = 'UUUwUUU\n'
        archivo.seek(0)
        archivo.writelines(texto)
        archivo.close()
        print(texto)

    else:
        print('No se encontro el archivo')

#modificar_datos()

'''
La siguiente instruccion sobreescribe todo lo que haya dentro del archivo por nada.
'''

def eliminar_todos_los_datos():
    archivo = open('UwU.txt', 'w')
    archivo.close()

eliminar_todos_los_datos()