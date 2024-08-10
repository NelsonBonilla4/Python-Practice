'''
Definición: polimorfismo (en POO) es la capacidad que tienen ciertos lenguajes para hacer que, 
al enviar el mismo mensaje (o, en otras palabras, invocar al mismo método) desde distintos objetos, 
cada uno de esos objetos pueda responder a ese mensaje (o a esa invocación) de forma distinta.
'''

class Persona(object):

    def __init__(self,nombre):
        self.nombre = nombre

    def moverse(self):
        print(f'Yo {self.nombre} ando caminando.')
    
class Atleta(Persona):

    def moverse(self):
        print(f'Yo {self.nombre} ando corriendo')

class Ciclista(Persona):

    def moverse(self):
        print(f'Yo {self.nombre} ando en bicicleta')