# Podemos crear  nuestras propias excepciones, heredando de la super clase 'Exception' y trabajando a partir
# de ese punto.
class OperadorException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


# Lanzando excepciones
# Con 'raise' lanzamos excepciones de una manera personalizada, es como si personalizaramos el mensaje 
# De error
def divi(a,b):
    if b == 0:
       raise OperadorException('Error: No es posible dividir entre cero')
        #raise ZeroDivisionError('Error: No es posible dividir entre cero')

    else:
        return a/b

divi(4,0)