'''
Reto para el Estudiante:
Hola mi querido estudiante, tengo un repo para ti, resuelve el siguiente problema antes de pasar a la solución 
que está en la siguiente clase. Por más fácil o difícil que parezca pon en practica todo lo que aprendiste y yo se que lo puede resolver,
lo impórtate es llegar a la solución porque se que lo puedes resolver de manera distinta a lo que veras en solución.

1. Crear un módulo figuras.py, y dentro crea clases como Figura, Rectangulo, Circulo y la función probar_figura.

2. Crear una clase Figura, con atributo nombre. Crear también el constructor de la clase 
y los métodos necesarios área y el perímetro con instrucción pass.

3. Crear otra clase Rectángulo que herede de la clase Figura, con atributos base y altura. 
Crear también el constructor de la clase y reescribe los métodos de la clase Figura 
para calcular el área y el perímetro.

4. Crear otra clase Circulo que herede de la clase Figura, con atributo radio.
Crear también el constructor de la clase y reescribe los métodos de la clase Figura para calcular el área 
y el perímetro.

5. Crear una función probar_figura donde reciba un objeto para probar diferentes figuras como rectángulo o circulo. 
E imprima el estado del objeto y como también el área y perímetro.

6. Crear un módulo principal main.py, luego importa desde el modulo figuras las clases Rectángulo, Circulo 
y la función probar_figura.

7. Crear la función principal que puede ser main() y el punto de entrada de la aplicación de Python 
y llama a ejecutar la función main().

8. Dentro de la función main() crea un sistema que tenga un bucle infinito y 
también tenga un menú de navegación donde las opciones sean 1-Rectangurlo 2-Circulo 4-Salir

9. En la opción 1 pide al usuario que ingrese base y altura del rectángulo y 
crea un objeto de rectángulo y ese objeto envía al funcion probar_figura()

10. En la opción 2 pide al usuario que ingrese el radio del circulo y 
crea un objeto de circulo y ese objeto envía al función probar_figura()

11. En la opción 3 termina el bucle infinito y se cierra el programa.
'''
import math as m

class Figura:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f'Nombre: {self.nombre}'

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(nombre='Rectangulo')
        # La siguiente linea nos muestra una forma para obtener el nombre de la clase
        #self.nombre = __class__.__name__
        self.base = base
        self.altura = altura
    
    def area(self):
        self.area = self.base * self.altura
        print(f'El area del rectangulo es de {self.area}m2')

    def perimetro(self):
        self.perimetro = (2 * self.base) * (2 * self.altura) 
        print(f'El perimetro del rectangulo es de {self.perimetro}m')

    def __str__(self):
        return super().__str__() + f'\nBase: {self.base}\nAltura: {self.altura}'


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__(nombre='Circulo')
        self.radio = radio

    def area(self):
        self.area = round((m.pi * (self.radio ** 2)), 2)
        print(f'El area del circulo es de {self.area}m2')

    def perimetro(self):
        self.perimetro = round((2 * m.pi * self.radio), 2)
        print(f'El perimetro del circulo es de {self.perimetro}m')

    def __str__(self):
        return super().__str__() + f'\nRadio: {self.radio}'

def probar_figura(figura_xd):
    if figura_xd == Rectangulo:
        base = int(input('Ingrese la base del rectangulo: '))
        altura = int(input('Ingrese la altura del rectangulo: '))
        rectangulino = Rectangulo(base,altura)
        print(rectangulino)
        rectangulino.area()
        rectangulino.perimetro()

    elif figura_xd == Circulo:
        radio = int(input('Ingrese el radio de su circulo: '))
        circulino = Circulo(radio)
        print(circulino)
        circulino.area()
        circulino.perimetro()     